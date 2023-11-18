from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    def get_permissions(self):
        permission_classes = {
            'GET': [AllowAny()],
            'POST': [IsAuthenticated()],
        }
        return permission_classes.get(self.request.method, [])
        
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            # Allow any user to retrieve (GET) the menu item
            return [AllowAny()]
        else:
            # For other methods (e.g., PUT and DELETE), check if the user is a manager
            return [IsAuthenticated()]
    
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()    
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
