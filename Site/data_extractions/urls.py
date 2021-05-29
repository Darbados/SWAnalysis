from django.urls import path
from . import views

app_name = 'Site'

urlpatterns = [
    path('exports', views.exports, name='exports'),
    path('save-collection', views.save_collection_data, name='save_collection_data'),
    path('download/<int:export_id>/export', views.export_download, name='export_download'),
    path('inspect/<int:export_id>/export', views.export_inspect, name='export_inspect'),
]
