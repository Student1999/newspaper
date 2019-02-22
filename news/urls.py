from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.index,name="index"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('single_post', views.single_post,name="single_post"),
    path('catagories_post', views.catagories_post,name="catagories_post"),
    ]
