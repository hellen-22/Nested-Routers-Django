from rest_framework import serializers


from .models import *

class CommentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        blog_id = self.context['blog_id']
        blog = Blog.objects.get(id=blog_id)

        comment= Comment.objects.create(blog=blog, **validated_data)

        return comment

    class Meta:
        model = Comment
        fields = ['id', 'content']

class BlogSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'description', 'content', 'comment']
