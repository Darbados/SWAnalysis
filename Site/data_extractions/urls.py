from django.urls import path
from . import views

app_name = 'data_extractions'

urlpatterns = [
    path('exports', views.exports, name='exports'),
    path('fetch-collection', views.fetch_collection_data, name='fetch_collection_data'),
]
