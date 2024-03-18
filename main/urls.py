from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login.as_view()),
    path('get_distance/', Get_Distance.as_view()),
]
