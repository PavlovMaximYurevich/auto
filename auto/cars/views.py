from django.shortcuts import render

from cars.models import Mark, ModelCar

from .loadxml import CAR_DICT


def update_autoru_catalog(request):

    for key, value in CAR_DICT.items():
        auto = Mark.objects.create(brand_auto=key)

        for models in value:
            model = ModelCar.objects.create(model_pk=auto, car_model=models)

    context = {
        'auto': auto,
        'models': model,
    }
    return render(request, 'cars/base.html', context=context)


