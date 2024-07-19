from rest_framework import serializers
from .models import Post

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        post = Post.objects.create(
            title=validated_data['title'],
            content=validated_data['content'],
            author=validated_data['author'],
            published_date=validated_data['published_date']
        )
        post.save()
        return post

class RetrievePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"