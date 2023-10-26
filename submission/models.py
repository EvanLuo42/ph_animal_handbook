from django.db import models


class Submission(models):
    id = models.UUIDField(primary_key=True)
    email = models.EmailField()
    animal_name = models.CharField(max_length=30)
    animal_image = models.ImageField()
    animal_category = models.CharField(max_length=50)
    animal_features = models.TextField(max_length=100)
