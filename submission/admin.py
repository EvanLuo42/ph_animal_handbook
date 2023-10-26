from django.contrib import admin
from django.db.models import QuerySet

from animals.models import Animal
from submission.models import Submission


@admin.action(description='Accept a submission and move it to the animal list')
def accept_submission(model_admin, request, queryset: QuerySet):
    for submission in queryset:
        Animal.objects.create(
            name=submission.animal_name,
            image=submission.animal_image,
            category=submission.animal_category,
            features=submission.animal_features
        )
        submission.delete()


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['animal_name', 'email']
    ordering = ['animal_name']
    actions = [accept_submission]


admin.site.register(Submission, SubmissionAdmin)
