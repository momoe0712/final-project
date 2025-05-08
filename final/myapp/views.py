from django.shortcuts import render
from .models import Menu,Booking
from .serializers import menuSerializer, bookingSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = bookingSerializer

def index(request):
    return render(request, "index.html", {})
