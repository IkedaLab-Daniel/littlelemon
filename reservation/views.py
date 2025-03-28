from django.shortcuts import render
from django.http import HttpResponse

# * DRF Stuffs
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# * Models stuffs
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

def home(request):
    return render(request, 'index.html', {})

#   API VIEW
class BookingView(APIView):

    def get(self, request):
        items = Booking.objects.all()   # queryset
        serializer = BookingSerializer(items, many= True) # model calss, serializer class
        return Response(serializer.data)

class MenuView(APIView):

    def get(self, request):
        items = Menu.objects.all() 
        serializer = MenuSerializer(items, many= True) # model calss, serializer class
        return Response(serializer.data)

# Generics
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # permission_classes = [permission.IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingItemView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleBookingItemView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer