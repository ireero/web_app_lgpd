from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/cadastro/', views.cadastro, name='cadastro'),
    path('quiz/', views.quiz, name='quiz'),
]
