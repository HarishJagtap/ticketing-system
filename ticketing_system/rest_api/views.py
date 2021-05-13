from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView

from .serializers import UserSerializer, TicketListSerializer, TicketSerializer
from .login.token_manager import TokenManager
from .response import login_response, ticket_response
from .ticket.decorators import fetch_requested_pageno
from .models import Ticket


class UserLogin(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # TokenManager takes care of creating new users and 
            # verifying password of old users, and returns access token 
            # only if user is verified.
            # Throws exception if unverified user tries to obtain access token

            tm = TokenManager(
                serializer.validated_data['username'], 
                serializer.validated_data['password'])
            try:
                access_token = tm.get_access_token()
            except:
                return login_response.incorrect_password_response()
                    
            return login_response.access_token_response(access_token)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketList(APIView):

    @fetch_requested_pageno
    def get(self, request, page):
        count = 20
        from_pk = (page - 1) * count
        to_pk = page * count - 1
        
        query_set = Ticket.objects.all()
        if from_pk < 0 or from_pk >= query_set.count():
            return Response(status=status.HTTP_404_NOT_FOUND)

        tickets = query_set[from_pk:to_pk+1].all()
        serializer = TicketListSerializer(tickets, many=True)

        next_link = None
        prev_link = None

        if to_pk < query_set.count() - 1:
            next_link = '{}?page={}'.format(
                    request.build_absolute_uri().split('?')[0],
                    page + 1)

        if from_pk > 0:
            prev_link = '{}?page={}'.format(
                    request.build_absolute_uri().split('?')[0],
                    page - 1)

        return ticket_response.paginated_ticket_list_response()(
                next_link, prev_link, serializer.data)

    def post(self, request):
        serializer = TicketSerializer(data=request.data, 
                context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketDetail(APIView):

    def get(self, request, pk):
        try:
            ticket = Ticket.objects.get(pk=pk)
        except ticket.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TicketSerializer(ticket)
        return Response(serializer.data)