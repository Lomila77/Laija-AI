from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AI(models.Model):
    name = models.CharField(max_length=20)
    back_story = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ais")
    personality = models.TextField()

    def __str__(self) -> str:
        return self.title
