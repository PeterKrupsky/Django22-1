from django.urls import path
from . import views

app_name = 'site_app'

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('page/<int:pk>/', views.page, name='page'),
]
