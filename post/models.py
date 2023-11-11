from django.db import models
import uuid

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),blank=False,null=False,primary_key=True)
    title= models.CharField(max_length=200,null=True)
    date=models.DateField(max_length=20)
