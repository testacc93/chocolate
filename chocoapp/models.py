from django.db import models

class Chocolate(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    description = models.CharField(max_length=256, blank=True)
    image = models.ImageField(upload_to='chocoimages',height_field=None,null=True, width_field=None)
    keyword = models.CharField(max_length=64, blank=True, help_text='Keyword to filter item. For eg. rum, dry fruits..')
    amazon_url = models.CharField(max_length=50, default='https://www.instagram.com/e_trunk_/')
    def __str__(self):
        return self.name

class Query(models.Model):

    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = "Queries"