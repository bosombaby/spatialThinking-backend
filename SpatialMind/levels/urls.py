from django.urls import path

from . import views

app_name = 'levels'
urlpatterns = [
    path('question', views.getLevelsQuestion, name='question'),
]
