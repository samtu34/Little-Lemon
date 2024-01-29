from django.contrib import admin 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet  # Adjust the import based on your actual project structure
 

# Create a router and register the BookingViewSet
router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),  # Include the base restaurant app URLs
    path('restaurant/menu/', include('restaurant.urls')),  # Include the restaurant app's URLs for menu
    path('restaurant/booking/', include(router.urls)), # Include the router's URLs in the project's URL patterns
    path('auth/', include('djoser.urls')),  # Djoser authentication endpoints
    path('auth/', include('djoser.urls.authtoken')),  # Djoser token authentication endpoints
    # other urlpatterns...
]




