from rest_framework import serializers
from .models import Album,Song

class AlbumSerializer(serializers.Serializer):

    class Meta:

        model = Album
        fields = ('album_title',)

class SongSerializer(serializers.Serializer):

    class Meta:

        model = Song
        fields = '__all__'

