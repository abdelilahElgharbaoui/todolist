from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-todo', views.submit_todo, name='submit-todo'),
    path('complete-todo/<int:pk>/', views.complete_todo, name='complete-todo'),
    path('uncomplete-todo/<int:pk>/', views.uncomplete_todo, name='uncomplete-todo'),
    path('delete-todo/<int:pk>/', views.delete_todo, name='delete-todo'),
    path('disconnect/', views.disconnect_view, name='disconnect'),
]
