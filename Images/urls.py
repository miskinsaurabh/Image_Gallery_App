from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('view_image/<str:x>/', views.addImage, name='view_image'),
    path('add_image/', views.addImage, name='add_image'),

]