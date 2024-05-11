from django.urls import path

from . import views

app_name = 'feedback'
urlpatterns = [
    path('record/create', views.createRecord, name='createRecord'),
]
