from rest_framework import generics, viewsets
from notes_app.models import notes
from .serializer import NotesSerializer

class NotesView(viewsets.ModelViewSet):
    queryset = notes.objects.all()
    serializer_class = NotesSerializer