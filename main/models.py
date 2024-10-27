from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description


from django.db import models

class Picture(models.Model):
    description = models.TextField()  # Field for the picture's description
    image = models.ImageField(upload_to='pictures/')  # Field for the image

    def __str__(self):
        return self.description  # This will show the description in the admin interface
