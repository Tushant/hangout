from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('login', views.Login.as_view()),
]
