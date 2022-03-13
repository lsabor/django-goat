from django.urls import path
from . import views


# THIS NAME IS IMPORTANT, it's what django looks for
# URLConf module - URL configuration
urlpatterns = [
    path('',                # this is the Route - the url that when called returns the view
    views.say_hello,         # Do not call the function, merely pass it
    ),
    path('fart/', views.say_goodbye),
    path('hi/',   views.hi),
]












