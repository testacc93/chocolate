# Generated by Django 3.2.8 on 2021-10-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocoapp', '0004_alter_chocolate_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolate',
            name='image',
            field=models.ImageField(null=True, upload_to='chocoimages'),
        ),
    ]
