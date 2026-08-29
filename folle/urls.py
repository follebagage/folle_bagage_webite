from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from pages.views import health

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('health/', health, name='health'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
