# Generated by Django 3.1.3 on 2021-01-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='is_favorites',
            field=models.BooleanField(default=False),
        ),
    ]
