from django.db import models


# Create your models here.
class Position(models.Model):
    objects = None
    position = models.CharField(max_length=50)
    about = models.TextField(default='')

    def __str__(self):
        return self.position


class User(models.Model):
    username = models.CharField(max_length=50)
    regno = models.CharField(max_length=20)
    email = models.EmailField
    password = models.CharField(max_length=20)
    fingerprint1 = models.CharField(max_length=10000)
    fingerprint2 = models.CharField(max_length=10000)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    voted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Candidate(models.Model):
    name = models.CharField(max_length=50)
    Description = models.TextField()
    image = models.ImageField(upload_to='Vote/static/Vote', blank=True)
    position = models.OneToOneField(Position, on_delete=models.CASCADE, related_name='pos', default=1, blank=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
