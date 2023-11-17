from django.db import models


class Mark(models.Model):
    brand_auto = models.CharField(
        'Марка автомобиля',
        # on_delete=models.CASCADE,
        max_length=200
    )


class ModelCar(models.Model):
    model_auto = models.ForeignKey(
        Mark,
        on_delete=models.CASCADE,
        verbose_name='Модель автомобиля'
    )
