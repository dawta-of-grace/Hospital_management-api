from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class patient(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE,  null=True, blank=True)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    contact = models.CharField(max_length=15)


    def __str__(self):
        return self.full_name