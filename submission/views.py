from PIL import Image
from django.http import JsonResponse

from submission.forms import SubmitAnAnimal
from submission.models import Submission


def submit_an_animal(request):
    if request.method != 'POST':
        return JsonResponse({}, status=405)

    form = SubmitAnAnimal(request.POST)

    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    email = form.clean_email()
    animal_name = form.clean_animal_name()
    animal_image = form.cleaned_data.get('animal_image')
    animal_category = form.cleaned_data.get('animal_category')
    animal_features = form.cleaned_data.get('animal_features')

    Submission.objects.create(
        email=email,
        animal_name=animal_name,
        animal_image=Image.open(animal_image).getdata(),
        animal_category=animal_category,
        animal_features=animal_features
    )
