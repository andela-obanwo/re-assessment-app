from django.db import models

# Create your models here.
class Birthday(models.Model):
    date = models.DateField()
    celebrates = models.BooleanField(default=True)

    def __str__(self):
        return "{}:{}".format(self.date, self.celebrates)