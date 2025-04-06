from django import forms
from .models import Document,DeletedDocument

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['subject', 'content']

class DeletedDocumentForm(forms.ModelForm):
    class Meta:
        model = DeletedDocument
        fields = ['subject', 'content']

