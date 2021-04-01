from django.contrib.auth.models import User
from rest_framework import serializers
from comment.models import Comment
from rest_framework.serializers import SerializerMethodField

from post.models import Post


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        exclude=["created",] #fields dan harici sadece istemediğimizi verip geri kalan hepsini alırız.

    def validate(self, attrs):
        if(attrs["parent"]):
            if attrs["parent"].post != attrs["post"]:
                raise serializers.ValidationError("something went wrong")
        return attrs
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "id",
            "email"
        ]
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=[
            "title",
            "slug",
        ]
class CommentListSerializers(serializers.ModelSerializer):
    replies=SerializerMethodField()
    user=UserSerializers()
    post=PostSerializers()
    class Meta:
        model=Comment
        fields="__all__"
        depth=1
    def get_replies(self,obj):
        if obj.any_children:
            return CommentListSerializers(obj.children(),many=True).data

class CommentDeleteUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=[
            "content"
        ]