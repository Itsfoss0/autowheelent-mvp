from django.db import models

# Create your models here.

class Car(models.Model):
    """
    Car model
    """
    id = models.IntegerField(primary_key=True)
    color = models.TextField(max_length=30)
    car_title = models.TextField(max_length=30, null=False)
    city = models.TextField(max_length=30, null=False)
    model = models.TextField(max_length=30)
    year = models.DateField(auto_created=True, unique=False)
    body_style = models.TextField(max_length=30)
    fuel_type = models.TextField(max_length=30)
    is_featured = models.TextField(max_length=30)
    

    def create(self):
        self.save()