from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

def validate_number(number):
    if not number.isdigit(number) or len(number) != 11 :
        raise ValidationError('sorry this number not valid')


class User(AbstractUser):
    full_name=models.CharField(max_length=120)
    job=models.CharField(max_length=120)
    image=models.ImageField(upload_to='photo_user')
    phone=models.CharField(max_length=25,validators=[validate_number])
    details=models.TextField(max_length=750)

    first_name=None
    last_name=None

    def __str__(self):
        return self.full_name
