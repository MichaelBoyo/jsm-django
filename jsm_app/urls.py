from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('income/', views.income, name='income'),
    path('expense/', views.expense, name='expense'),
    path('todo/', views.todo, name='todo'),
    path('note/', views.note, name='note'),
    path('userpage/', views.userpage, name='userpage'),

]
