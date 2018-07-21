from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_publish = models.DateTimeField(blank=True,null=True)
    content = models.TextField(max_length=2000)
    def __str__(self):
        return self.title