# Generated by Django 3.2.8 on 2021-10-25 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocoapp', '0006_chocolate_keyword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolate',
            name='keyword',
            field=models.CharField(blank=True, help_text='Keyword to filter item. For eg. rum, dry fruits..', max_length=64),
        ),
    ]
