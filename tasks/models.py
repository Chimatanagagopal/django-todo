from django.db import models

# Create your models here.
class userRegister(models.Model):
    Name=models.CharField(max_length=20)
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=8)
    def __str__(self):
       return self.Name

class studentData(models.Model):
    Name=models.CharField(max_length=25)
    department=models.CharField(max_length=25)
    phoneNumber=models.CharField(max_length=25)
    def __str__(self):
        return self.Name

    