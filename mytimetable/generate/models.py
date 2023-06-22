from django.db import models

# Create your models here.
class TotalActivities(models.Model):
    total = models.IntegerField()


class Subject(models.Model):
    name= models.CharField(max_length=30)
    hours = models.IntegerField()

    def __str__(self):
        return self.name