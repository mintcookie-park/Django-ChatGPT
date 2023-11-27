from rest_framework import serializers
from .models import ChatingRoom

class ConversationSerializer(serializers.Serializer):
    prompt = serializers.CharField()
    response = serializers.CharField()

class ChatingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatingRoom
        fields = ['name', 'user']