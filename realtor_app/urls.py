from django.urls import path
from . import views

urlpatterns = [
    path('', views.PropertyList.as_view(), name='home'),
    path('property/<int:pk>/', views.PropertyDetails.as_view(), name='property_details'),
    path('about/', views.AboutView.as_view(), name='about'),
]