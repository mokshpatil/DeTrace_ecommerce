# Generated by Django 5.0.6 on 2024-06-10 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customer_is_vendor_vendor_is_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_vendor',
            field=models.BooleanField(default=False),
        ),
    ]
