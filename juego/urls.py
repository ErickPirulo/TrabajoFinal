from django.urls import path
from . import views

urlpatterns = [
    path('', views.juego, name='juego'),
]

"""urlpatterns = [
    path('', views.juego, name='juego'),

]"""