from django.shortcuts import render
from django.http.response import Http404
from .models import Comments, Replies
from .serializers import CommentsSerializer, RepliesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CommentsViews(APIView):
    
    def get(self, request): #get all comments
        comment = Comments.objects.all()
        serializer = CommentsSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request): #create comment
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RepliesViews(APIView):

    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk): #get relative replies
        replies = Replies.objects.all()
        reply = replies.filter(comment_id=pk)
        serializer = RepliesSerializer(reply, many=True)
        return Response(serializer.data)

    def post(self, request, pk): #reply to comment
        commentpk = self.get_object(pk)
        if request.method == "POST":
            content = request.data
            comment = commentpk
            reply = Replies(content=content, comment=comment)
            reply.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        
class Likes(APIView):

    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def patch(self, request, pk):
        comment = self.get_object(pk)
        comment.like_counter+=1
        comment.save()
        serializer = CommentsSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class Dislikes(APIView):

    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def patch(self, request, pk):
        comment = self.get_object(pk)
        comment.dislike_counter+=1
        comment.save()
        serializer = CommentsSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)