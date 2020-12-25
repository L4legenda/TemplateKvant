from django.urls import path
from . import views

urlpatterns = [
    path('', views.news),
    path('create', views.create, name='create'),

]
