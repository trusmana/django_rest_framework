from django.shortcuts import render
from rest_framework import viewsets
from .models import Song
from .serializers import SongSerializer

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
