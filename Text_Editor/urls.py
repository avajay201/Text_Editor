from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='Index'),
    path('about', views.about, name='About'),
    path('contact', views.contact, name='Contact'),
    path('result/', views.result, name='Result'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)