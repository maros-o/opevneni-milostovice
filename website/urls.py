from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('klub', views.Klub),
    path('galerie/<str:url>', views.Galerie),
    path('galerie/<str:url1>/<str:url2>', views.GalerieViews),
    path('<str:url>', views.Error),
]