"""Define urls pattern for blog"""

from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
]