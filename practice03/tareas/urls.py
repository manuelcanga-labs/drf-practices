from django.urls import path

from tareas.views import CreateUser

urlpatterns = [
    path("users/", CreateUser.as_view() , name="create_users"),
]