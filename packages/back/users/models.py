from django.db import models

class User(models.Model):
    # ais
    username = models.CharField(max_length=50)
