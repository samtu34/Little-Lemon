from django.contrib import admin 
from django.urls import path
from .views import MenuItemView, SingleMenuItemView #This is for the API url created in views
#from .views import sayHello 
from . import views
from rest_framework.authtoken.views import obtain_auth_token    #import obtain_auth_token view for the authentication 



urlpatterns = [
    path('', views.index, name='index'),#url pattern and path for the index html file
    path('menu/', MenuItemView.as_view(), name='menu-list-create'), #path for menu item created in views 
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'), #where <int:pk> is the primary key of the menu item
    path('api-token-auth/', obtain_auth_token)
]



