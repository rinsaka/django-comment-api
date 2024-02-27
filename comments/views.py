from django.shortcuts import render
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from .paginations import LargeResultsSetPagination

# Create your views here.

# class CommentList(generics.ListAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# class CommentDetail(generics.RetrieveAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = LargeResultsSetPagination

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
