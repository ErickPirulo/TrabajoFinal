from django.urls import path
from usuario.views import registro, login, logout, home, index


urlpatterns = [
    path('registro', registro),
    path('login', login),
    path('logout', logout),
    path('', index),

]