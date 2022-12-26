from django.db import models

class Session(models.Model):
    application = models.CharField(max_length=40, blank=True)
    user_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=60)

