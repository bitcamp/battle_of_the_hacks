from django.db import models

# Create your models here.
class Registrant(models.Model):
    first_name = models.CharField(max_length = 500)
    last_name = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    school = models.CharField(max_length = 500)
    image = models.CharField(max_length = 500)

    def __str__(self): 
        return self.first_name + "  " + self.last_name + " " + self.email + " " + self.school + " " + self.image

