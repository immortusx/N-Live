from django import views
from django.contrib import admin
from django.urls import path, include
from nliveapp import views
urlpatterns = [
    path('', views.index, name="home"),
    path('sports', views.sports, name="sports"),
    path('entertainment', views.entertainment, name="entertainment"),
    path('business', views.business, name="business"),
    path('technology', views.technology, name="technology"),
    path('startup', views.startup, name="startup"),
    path('politics', views.politics, name="politics"),
    path('education', views.education, name="education"),
    path('national', views.national, name="national"),
    path('miscellaneous', views.miscellaneous, name="miscellaneous"),
    path('world', views.world, name="world"),
    path('hatke', views.hatke, name="hatke"),
    path('about', views.about, name="about"),
]
