from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('people/', include('people.urls', namespace='people')),
    path('data-collections/', include('data_collections.urls', namespace='data_collections')),
    path('django-admin/', admin.site.urls),
    path('worlds/', include('worlds.urls', namespace='worlds')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
