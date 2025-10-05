from django.urls import path
from . import views

urlpatterns = [
    # When someone visits the base URL of this app, run the hello_world view.
    path('', views.home, name='home'),
    path('notifications/', views.notice, name='notice'),
    path('timetable/', views.timetable, name='timetable'),
    path('events/', views.events, name='events'),

    path('resources/', views.resources, name='resources'),
    path('career/', views.career, name='career'),
    path('achievements/', views.achive, name='achive'),

]