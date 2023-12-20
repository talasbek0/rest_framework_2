from django.db import models


class Cars(models.Model):
    title = models.CharField(max_length=40)
    off_roads = models.BooleanField
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    seating_capacity = models.PositiveIntegerField()
    four_wheel_drive = models.BooleanField(default=True)
    ground_clearance = models.DecimalField(max_digits=5, decimal_places=2)
    off_road = models.CharField(max_length=100)
    additional_features = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class RentCar(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    select_car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    email = models.EmailField()
    male = models.CharField(max_length=1, choices=GENDER_CHOICES)
    start_rental = models.DateTimeField(auto_now_add=True)
    end_rental = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'