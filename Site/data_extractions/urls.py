from django.urls import path
from . import views

app_name = 'data_extractions'

urlpatterns = [
    path('exports', views.exports, name='exports'),
    path('export-collection', views.export_collection_data, name='export_collection_data'),
]
