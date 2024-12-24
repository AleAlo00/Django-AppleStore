from django.urls import path
from . import views

urlpatterns = [
    path('iPad/', views.iPads, name='iPhone'),
    path('iPad/iPadDetails/<int:iPad_id>/', views.iPadDetails, name='iPadDetails'),
]