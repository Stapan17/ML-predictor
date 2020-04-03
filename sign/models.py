from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=10)
    age = models.CharField(max_length=10)

    def __str__(self):
        return self.name

