from django.shortcuts import render

from cars.models import Mark, ModelCar

from .loadxml import CAR_DICT


def update_autoru_catalog(request):

    for key, value in CAR_DICT.items():
        auto = Mark.objects.create(brand_auto=key)

        for models in key:
            model = ModelCar.objects.create(car_model=models, pk)

    context = {
        'auto': auto,
        'models': model,
    }
    return render(request, 'cars/base.html', context)


