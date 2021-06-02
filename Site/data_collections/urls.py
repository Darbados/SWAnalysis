from django.urls import path
from . import views

app_name = 'data_collections'

urlpatterns = [
    path('', views.index, name='index'),
    path('save-collection', views.save_collection_data, name='save_collection_data'),
    path('<int:collection_id>/download', views.download, name='download'),
    path('<int:collection_id>/inspect', views.inspect, name='inspect'),
    path('<int:collection_id>/value-counts', views.collection_value_counts, name='value_counts'),
    path('<int:collection_id>/delete', views.delete, name='delete'),
    path('<int:collection_id>/resolve', views.resolve, name='resolve'),
]
