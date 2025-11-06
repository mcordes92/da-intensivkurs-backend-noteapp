from rest_framework import serializers
from notes_app.models import notes

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = notes
        fields = ['id', 'title', 'content', 'marked', 'trash'] 