from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class passwordUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

