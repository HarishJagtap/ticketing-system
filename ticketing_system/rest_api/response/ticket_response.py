from rest_framework.response import Response
from rest_framework import status


def paginated_ticket_list_response(next_link, prev_link, ticket_list):
    return Response(
        {
            'next': next_link,
            'previous': prev_link,
            'result': ticket_list
        })
