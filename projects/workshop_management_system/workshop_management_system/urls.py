from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('apps.home.urls')),
                  path('accounts/', include('apps.account.urls')),
                  path('', include('social_django.urls', namespace='social')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
