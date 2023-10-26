from django.forms import Form, fields

from animals.models import Animal


class SubmitAnAnimal(Form):
    email = fields.EmailField(
        required=True,
        error_messages={
            'required': 'ph_animal_handbook.submission.email.required'
        }
    )

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

    def clean_email(self):
        email_suffix = self.cleaned_data.get('email').split('@')[1]
        if not email_suffix == 'shphschool.com':
            raise fields.ValidationError('ph_animal_handbook.submission.email.not_school_email')

        return self.cleaned_data.get('email')

    def clean_animal_name(self):
        if Animal.objects.filter(name=self.animal_name).exists():
            raise fields.ValidationError('ph_animal_handbook.submission.animal_name.exists')
        return self.cleaned_data.get('animal_name')
