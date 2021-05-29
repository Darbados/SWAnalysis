from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    # path('characters/', include('characters.urls', namespace='characters')),
    path('data-extractions/', include('data_extractions.urls', namespace='data_extractions')),
    path('django-admin/', admin.site.urls),
    # path('worlds/', include('worlds.urls', namespace='worlds')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
