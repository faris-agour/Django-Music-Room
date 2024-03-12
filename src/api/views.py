from django.http import HttpResponse
from rest_framework import generics

from .models import Room
from .serializers import RoomSerializer


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# Create your views here.
