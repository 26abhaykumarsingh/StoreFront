from django.urls import path
from . import views

# Map URLs to views functions

# URLConf
urlpatterns = [
  path('hello/', views.say_hello)
]

