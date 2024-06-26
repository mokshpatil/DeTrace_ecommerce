# Generated by Django 5.0.6 on 2024-06-10 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_is_active_customuser_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_vendor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vendor',
            name='is_vendor',
            field=models.BooleanField(default=True),
        ),
    ]
