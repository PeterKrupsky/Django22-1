from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'site_app'
urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('page/<int:pk>/', views.page, name='page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
