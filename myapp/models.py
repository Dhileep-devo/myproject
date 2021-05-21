from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feed(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(blank=False, max_length=500)

class FeedFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)