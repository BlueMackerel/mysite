from django.contrib import admin
from .models import Document,DeletedDocument

# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class DeletedDocumentAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Document,DocumentAdmin)
admin.site.register(DeletedDocument,DeletedDocumentAdmin)


