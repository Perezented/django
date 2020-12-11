from django.urls import path

from . import views


app_name = 'polls'
# pretty much created a route
urlpatterns = [
    path('', views.index, name='index'),
]
