from django.urls import path
from . import views

urlpatterns = [
    # When someone visits the base URL of this app, run the hello_world view.
    path('', views.home, name='home'),
]