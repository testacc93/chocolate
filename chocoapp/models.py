from django.db import models

class Chocolate(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    description = models.CharField(max_length=256, blank=True)
    image = models.ImageField(upload_to='chocoimages',height_field=None,null=True, width_field=None)

    def __str__(self):
        return self.name