from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from favourite.models import Favourite

class FavouriteListCreateAPISerializer(ModelSerializer):
    class Meta:
        model=Favourite
        fields="__all__"


    def validate(self,attrs): ##eğer favorilere eklenen bir postu brdaha eklemek istersek böyle bir hata mesajı yazabiliriz
        queryset=Favourite.objects.filter(post=attrs["post"],user=attrs["user"])
        if queryset.exists():
            raise serializers.ValidationError("already add favorite")
        return attrs

class FavaouriteUpdateDestroyAPISerializer(ModelSerializer):
    class Meta:
        model=Favourite
        fields=[
            "content"
        ]