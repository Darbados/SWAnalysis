from django.urls import path
from . import views

app_name = 'Site'

urlpatterns = [
    path('exports', views.exports, name='exports'),
    path('export-collection', views.export_collection_data, name='export_collection_data'),
    path('download/<int:export_id>/export', views.export_download, name='export_download'),
]
