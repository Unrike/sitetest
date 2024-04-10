from django.db import models

class UserModel(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.age} aged {self.first_name} {self.second_name}"
