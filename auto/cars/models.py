from django.db import models


class Mark(models.Model):
    brand_auto = models.CharField(
        'Марка автомобиля',
        max_length=200
    )

    def __str__(self):
        return self.brand_auto


class ModelCar(models.Model):
    model_pk = models.ForeignKey(
        Mark,
        on_delete=models.CASCADE,
        related_name='auto'
    )
    car_model = models.CharField(
        'Модель автомобиля',
        max_length=200
    )
