from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.first_name
        return self.last_name
        return self.email
        return self.phone_number