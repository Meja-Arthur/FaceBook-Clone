from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # reason for read only is that when we created the post later we don't want to mess with the fields 
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields =('id', 'body', 'created_by', 'created_at_formatted',)