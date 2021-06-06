from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('lgout', views.logout, name='logout'),
    path('register', views.register, name='register'),
]
