from django.urls import path, include
from .views import NotesView

urlpatterns = [
    path('', NotesView.as_view({'get': 'list', 'post': 'create'}), name='notes-list'),
    path('<int:pk>/', NotesView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='notes-detail'),
]
