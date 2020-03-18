from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    #path('home/',views.home,name='home'),
    path('movie/<str:movie_id>/',views.movie,name='movie'),
    path('actor/<str:actor_id>/',views.actor,name='actor'),
    path('director/<str:name>/',views.director,name='director'),
    path('analytics/',views.analytics,name='analytics'),

]