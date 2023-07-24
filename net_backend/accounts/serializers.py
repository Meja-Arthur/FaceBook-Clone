from rest_framework import serializers
from .models import User, FriendlyRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id', 'name', 'email', 'friends_count',)
        
class FriendlyRequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = FriendlyRequest
        fields = ('id', 'created_by',)        
        #i think this id is for the user that has sent the request 