# todo/todo_api/urls.py : API urls.py
from django.urls import path
from .views import (
    TodoListApiView,
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
]
