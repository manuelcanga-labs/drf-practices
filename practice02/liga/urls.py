from django.urls import path

from .views import EquipoListCreate, EquipoRetrieve


urlpatterns = [
    path('', EquipoListCreate.as_view(), name="list_create"),
    path('<int:pk>/', EquipoRetrieve.as_view(), name="retrieve"),

]
