from rest_framework import serializers
from post.models import Post
class PostSerializer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )
    username=serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields=[
            "id",
            "username",
            "title",
            "content",
            "image",
            "url",
            "created"
        ]
    def get_username(self,obj):
        return str(obj.user.username)
class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=[
            "title",
            "content",
            "image",
        ]