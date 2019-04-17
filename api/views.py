from django.shortcuts import render
from rest_framework import viewsets
from .models import Song,Album
from .serializers import SongSerializer,AlbumSerializer

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class AlbumView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
