from django.db import models

# Create your models here.

class FeedbackModel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    message = models.TextField(max_length=500)
    place = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name
    
class SigninModel(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.email
    
class SignupModel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name 
    
class BookingModel(models.Model):
    name = models.CharField(max_length=25)
    age = models.CharField(max_length=2)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    email = models.EmailField(max_length=25)
    roomtype = models.CharField(max_length=10)
    paymentmethod = models.CharField(max_length=25)

    def __str__(self):
        return self.name