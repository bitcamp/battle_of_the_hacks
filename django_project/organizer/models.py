from django.db import models

# Create your models here.

class Attendee(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    school = models.CharField(max_length = 100)
    image = models.Charfield(max_length = 100)
