from django.db import models
from django.contrib.auth.models import AbstractUser


class TzUser(AbstractUser):
    email = models.EmailField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.username)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='media', default='defaultpost.jpg', blank=True, null=True)
    author = models.ForeignKey(TzUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} by {}".format(self.title, self.author)


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    author = models.ForeignKey(TzUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} commented {}".format(self.author, self.post)


