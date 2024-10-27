from django.db import models

class Picture(models.Model):
    description = models.TextField()  # Field for the picture's description
    image = models.ImageField(upload_to='pictures/')  # Field for the image

    def __str__(self):
        return self.description  # This will show the description in the admin interface
    

from django.contrib.auth.models import User
from django.db import models
from django_mysql.models import ListCharField  # Import ListCharField


from django.db import models
from django_mysql.models import ListCharField
from django.contrib.auth.models import User

from django.db import models
from django_mysql.models import ListCharField

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score1 = models.CharField(max_length=255, default='')
    score2 = models.CharField(max_length=255, default='')
    score3 = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.user.username

    def get_score1_list(self):
        return list(map(int, self.score1.split(','))) if self.score1 else []

    def get_score2_list(self):
        return list(map(int, self.score2.split(','))) if self.score2 else []

    def get_score3_list(self):
        return list(map(int, self.score3.split(','))) if self.score3 else []

    def set_score1_list(self, scores):
        self.score1 = ','.join(map(str, scores))
        print(','.join(map(str, scores)))

    def set_score2_list(self, scores):
        self.score2 = ','.join(map(str, scores))

    def set_score3_list(self, scores):
        self.score3 = ','.join(map(str, scores))




