from django.db import models

# Create your models here.
class Person(models.Model):
    genderlist = (('Male', 'Male'), ('Female', 'Female'))
    fullname = models.CharField(max_length=50, blank=False, null=False)
    gender = models.CharField(max_length=6, choices=genderlist)
    email = models.EmailField(max_length=200, blank=False, null=False)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.fullname
    

    