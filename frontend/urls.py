from django.conf import settings #add this
from django.conf.urls.static import static #add this
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", include('StoryTeller.urls')),
    path('admin/', admin.site.urls),
    path('', include ('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
