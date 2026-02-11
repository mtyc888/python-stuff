"""url patterns for meal plans"""

from django.urls import path
from . import views

app_name = "meal planner"
urlpatterns = [
    path('', views.index, name='index')
]