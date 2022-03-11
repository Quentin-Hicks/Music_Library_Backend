from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song

# Create your views here.
@api_view(['GET', 'POST'])
def songs_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        return Response('ok')

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    if request.method == 'GET':
        return Response('ok')

    elif request.method == 'PUT':
        return Response('ok')
    
    elif request.method == 'DELETE':
        return Response('ok')