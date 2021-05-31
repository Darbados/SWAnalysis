from django.urls import path
from . import views

app_name = 'worlds'

urlpatterns = [
    path('', views.index, name='index'),
]
