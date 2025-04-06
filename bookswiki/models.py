from django.db import models

# Create your models here.

class Document(models.Model):
    subject= models.CharField(max_length=200)
    content=models.TextField()
    modify_date_list=models.JSONField(null=True,blank=True)
    def __str__(self):
        return self.subject

class DeletedDocument(models.Model):
    subject= models.CharField(max_length=200)
    content=models.TextField()
    modify_date_list=models.JSONField(null=True,blank=True)
    def __str__(self):
        return self.subject

