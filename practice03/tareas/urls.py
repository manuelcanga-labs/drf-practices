from django.urls import path

from tareas.models import Tarea
from tareas.views import CreateUser, TareaEndpoint, TareasEndpoint

urlpatterns = [
    path("users/", CreateUser.as_view() , name="create_users"),
    path("tareas/<int:pk>/", TareaEndpoint.as_view(), name="tarea"),
    path("tareas/", TareasEndpoint.as_view(), name="tareas")
]