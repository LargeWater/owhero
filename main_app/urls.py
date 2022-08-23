from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('heroes/', views.hero_list, name='heroes_list'),
  path('heroes/<hero_name>', views.hero_detail, name='hero_detail'),
]