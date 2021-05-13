from rest_framework.response import Response
from rest_framework import status

def fetch_requested_pageno(func):
    
    def wrapper(self, request):
        page = 1

        if 'page' in request.GET:
            try:
                page = int(request.GET['page'])
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return func(self, request, page)

    return wrapper