from rest_framework import serializers

from .models import Ticket

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class TicketSerializer(serializers.Serializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketListSerializer(serializers.Serializer):
    class Meta:
        model = Ticket
        exclude = ['description']
