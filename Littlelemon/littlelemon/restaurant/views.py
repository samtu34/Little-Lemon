from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView # menu api/views.py
from .models import Menu # menu api/views.py
from .serializers import MenuSerializer # menu api/views.py
from rest_framework import viewsets # imported for the booking views set 
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated #for authentication 
from rest_framework.response import Response
from rest_framework.views import APIView

# your other imports...

# Create your views here.


#def sayHello(request):
 #return HttpResponse('Hello World')

#The views for the html file in the template 
def index(request):
 return render(request, 'index.html', {})

# restaurant/views.py

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):#view set allows to perfrom CRUD operations 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  # Set permission to IsAuthenticated

