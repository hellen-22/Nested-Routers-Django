from django.shortcuts import render
from rest_framework import viewsets


from .serializers import *
from .models import *


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {"blog_id": self.kwargs["blog_pk"]}
    
    def get_queryset(self):
        return Comment.objects.filter(blog_id=self.kwargs["blog_pk"])
        
    