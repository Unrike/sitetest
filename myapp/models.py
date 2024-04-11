from django.db import models
from django.forms import ValidationError

def validate_zero(value):
    if value < 0:
        raise ValidationError("Возраст не может быть отрицательным")

class UserModel(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0, validators=[validate_zero])

    def __str__(self) -> str:
        return f"{self.age} aged {self.first_name} {self.second_name}"
