from django.urls import path

from .views import UserLogin, TicketList, TicketDetail

urlpatterns = [
    path('login/', UserLogin.as_view(), name='user_login'),
    path('ticket/', TicketList.as_view(), name='ticket_list'),
    path('ticket/<int:pk>/', TicketDetail.as_view(), name='ticket_detail'),
]
