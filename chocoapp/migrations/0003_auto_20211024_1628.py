# Generated by Django 3.2.8 on 2021-10-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocoapp', '0002_chocolate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolate',
            name='description',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='chocolate',
            name='image',
            field=models.ImageField(upload_to='chocoimages'),
        ),
    ]
