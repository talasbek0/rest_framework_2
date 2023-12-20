from django.db import models
from django.core.validators import MaxValueValidator


class TourList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    next_day = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    tour = models.ForeignKey(TourList, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.tour}"


class About(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return f"История {self.title}"


class CustomTourRequest(models.Model):
    client_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    telegram_id = models.CharField(max_length=100, blank=True, null=True)
    desc = models.TextField()
    col_person = models.PositiveIntegerField()
    col_days = models.PositiveIntegerField()
    meat_option = models.CharField(max_length=20, choices=[('BB', 'Завтрак'), ('BB+L', 'Завтрак и обед'), ('BB+L+D', 'Завтрак, обед и ужин')])
    hotel_option = models.CharField(max_length=20, choices=[('2', 'Двухзвездочный отель'), ('3', 'Трехзвездочный отель'), ('4', 'Четырехзвездочный отель'), ('5', 'Пятизвездочный отель'), ('guesthouse', 'Гостевой дом')])
    transportation_option = models.CharField(max_length=50, choices=[('driver_car', 'Водитель + авто'), ('guide_driver_car', 'Гид + водитель + авто'), ('rent_car', 'Аренда машины')])
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.client_name} Тур забронирован"

