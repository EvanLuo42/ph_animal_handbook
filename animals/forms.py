from django.forms import Form, fields

from animals.models import Animal


class GetAnimalByName(Form):
    name = fields.CharField(
        required=True,
        error_messages={
            'required': 'ph_animal_handbook.animal.name.required'
        }
    )

    def clean_name(self):
        if not Animal.objects.filter(name=self.cleaned_data.get('name')).exists():
            raise fields.ValidationError('ph_animal_handbook.animal.name.not_exists')
        return self.cleaned_data.get('name')
