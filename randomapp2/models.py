from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Post(models.Model):
   title = models.CharField(max_length=255)
   summary = RichTextField()
   content = RichTextUploadingField()
   author = models.ForeignKey(User, on_delete=models.PROTECT)
   created_at = models.DateField(auto_now_add=True)
