from rest_framework import serializers

from .models import Ticket

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class TicketSerializer(serializers.Serializer):
    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        ticket = Ticket(**validated_data)
        ticket.author = self.context['user']
        ticket.save()
        return ticket

class TicketListSerializer(serializers.Serializer):
    class Meta:
        model = Ticket
        exclude = ['description']
