from distutils.command.upload import upload
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    content = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    CATAGORIES = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, default=title)
    email = models.EmailField()
    salary = models.IntegerField()
    details = models.TextField()
    available = models.BooleanField()
    catagory = models.CharField(max_length=100, choices=CATAGORIES)
    created_at = models.DateTimeField(default=now)
    image = models.ImageField(default='default.jpg', upload_to='images')
