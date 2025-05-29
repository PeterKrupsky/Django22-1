from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'site_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('site_app.urls')),  # <-- это важно!
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

