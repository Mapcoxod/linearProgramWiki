from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('dual_method/', dual_method, name='dual_method'),
    path('graphical_method/', graphical_method, name='graphical_method'),
]