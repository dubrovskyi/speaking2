from django.db import models


class User(models.Model):
    idd = models.CharField(max_length=18, null=True)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    level = models.CharField(max_length=10, null=True)
    question = models.CharField(max_length=50, null=True)
    connect = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
