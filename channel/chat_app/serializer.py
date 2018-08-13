from rest_framework import serializers
from .models import Channel, Post

class createChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['message','channel','created_by']
