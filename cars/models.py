from django.db import models

class Car(models.Model):
    """
    Car model
    """
    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=30)
    car_title = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    model = models.CharField(max_length=30)
    year = models.IntegerField()
    body_style = models.CharField(max_length=30)
    fuel_type = models.CharField(max_length=30)
    is_featured = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    car_image = models.ImageField(verbose_name='Car Image')

    def create(self):
        self.save()

    def __str__(self):
        """
        Representing the Car
        On the admin UI
        """
        return self.car_title