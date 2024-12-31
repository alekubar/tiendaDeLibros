from django.urls import path, include
from .views import login, perfil
from . import views

app_name = "usuario"

urlpatterns = [
    path("",login, name="login"),
    path("perfil/",perfil, name="perfil"),
    

]
