from rest_framework import serializers
from .models import Comments, Replies

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['videoId', 'content', 'like_counter', 'dislike_counter']

class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ['content', 'comment']