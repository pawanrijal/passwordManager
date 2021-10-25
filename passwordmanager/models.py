from django.db import models
from authUser.models import passwordUser
# Create your models here.
class Password(models.Model):
    websiteName=models.CharField(max_length=500)
    password=models.CharField(max_length=50)
    passworduser=models.ForeignKey(passwordUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.websiteName
