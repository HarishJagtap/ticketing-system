from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group

from .models import Ticket

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class TicketSerializer(serializers.ModelSerializer):
    impact = serializers.CharField()
    assignee = serializers.CharField(required=False)
    group = serializers.CharField(required=False)

    class Meta:
        model = Ticket
        exclude = ['author']

    def validate_impact(self, value):
        impact_int_value = None
        for a, b  in Ticket.Impact.choices:
            if b == value:
                impact_int_value = a
                break

        if impact_int_value is None:
            raise ValidationError(
                'Incorrect value. Expected {}'.format(
                    ', '.join([b for a, b in Ticket.Impact.choices])))
        return impact_int_value

    def validate_assignee(self, value):
        try:
            assignee = User.objects.get(username=value)
        except User.DoesNotExist:
            raise ValidationError('No user exists with this username')
        return assignee

    def validate_group(self, value):
        try:
            group = Group.objects.get(name=value)
        except Group.DoesNotExist:
            raise ValidationError('No group exists with this name')
        return group

    def create(self, validated_data):
        ticket = Ticket(**validated_data)
        ticket.author = self.context['user']
        ticket.save()
        return ticket

class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ['description']
