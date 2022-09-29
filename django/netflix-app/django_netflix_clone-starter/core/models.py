from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES=(
    ('All','All'),
    ('Kids','Kids')
)


MOVIE_CHOICES=(
    ('Seasonal','Seasonal'),
    ('Single','Single')
)
# Create your models here.

class CustomerUser(AbstractUser):
    profiles=models.ManyToManyField('Profile',null=True,blank=True)

class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4)

class Movie(models.Model):
    title=models.CharField(max_lenght=225)
    description=models.TextField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4)
    type=models.CharField(max_length=10, choices=MOVIE_CHOICES)
    videos=models.ManyToManyField('Video')
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES)

    