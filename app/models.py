from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    mobile = models.CharField(max_length=250, null=True, blank=True)
    password = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateTimeField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name