from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('contact/', views.contact, name='contact'),
    path('historie/', views.historie, name='historie'),
    path('datenschutz/', views.privacy, name='privacy'),
    path('impressum/', views.impressum, name='impressum'),
]
