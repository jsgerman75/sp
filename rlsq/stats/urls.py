from django.urls import path

from . import views


urlpatterns = [
        path('', views.home, name='home'),
        path('playerstats/', views.playerstats, name='playerstats'),
        path('top100/', views.top100, name='top100'),
]
