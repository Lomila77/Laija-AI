from django.db import models
from users.models import User

# Create your models here.
class Ai(models.Model):
    user: User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ais')
    name: str = models.CharField(max_length=50)
    story: str = models.TextField(max_length=500)

    class Meta:
        unique_together: list[str] = ['user', 'name']

    def __str__(self):
        return self.name
