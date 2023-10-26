from django.forms import Form, fields

from animals.models import Animal


class SubmitAnAnimal(Form):
    animal_name = fields.CharField(
        required=True,
        error_messages={
            'required': 'ph_animal_handbook.submission.animal_name.required'
        }
    )

    animal_image = fields.ImageField(
        required=True,
        error_messages={
            'required': 'ph_animal_handbook.submission.animal_image.required'
        }
    )

    animal_category = fields.CharField(
        required=True,
        error_messages={
            'required': 'ph_animal_handbook.submission.animal_category.required'
        }
    )

    animal_features = fields.CharField(
        required=True,
        error_messages={
            'required': 'ph_animal_handbook.submission.animal_features.required'
        }
    )

    def clean_animal_name(self):
        if Animal.objects.filter(name=self.animal_name).exists():
            raise fields.ValidationError('ph_animal_handbook.submission.animal_name.exists')
        return self.cleaned_data.get('animal_name')


