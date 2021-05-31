from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.index, name='index'),
    path('save-people', views.save_people, name='save_people'),
]
