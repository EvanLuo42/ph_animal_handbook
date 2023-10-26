from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='../images')
    category = models.CharField(max_length=50)
    features = models.TextField(max_length=100)

    def animal_to_dictionary(self):
        return {
            'name': self.name,
            'image': self.image.url,
            'category': self.category,
            'features': self.features
        }
