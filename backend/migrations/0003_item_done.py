# Generated by Django 5.0.2 on 2024-02-12 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
