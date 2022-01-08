from django.db import models

class URLRecord(models.Model):
    id = models.TextField(primary_key=True)
    short_url = models.TextField()
    long_url = models.TextField()