from django.http import JsonResponse

from animals.models import Animal
from animals.forms import GetAnimalByName


def get_all_animals(request):
    if not request.method == 'GET':
        return JsonResponse({}, status=405)

    return JsonResponse(
        {'animals': [Animal.animal_to_dictionary(animal) for animal in Animal.objects.all()]},
        status=200
    )


def get_animal_by_name(request, name):
    if not request.method == 'GET':
        return JsonResponse({}, status=405)

    form = GetAnimalByName(data={'name': name})

    if not form.is_valid():
        return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse(
        Animal.animal_to_dictionary(Animal.objects.get(name=form.clean_name())),
        status=200
    )
