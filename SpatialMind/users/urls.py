from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('get-async-routes', views.getAsyncRoutes, name='getAsyncRoutes'),
]
