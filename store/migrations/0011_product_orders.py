# Generated by Django 5.0.6 on 2024-06-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_qunatity_orderitems_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='orders',
            field=models.IntegerField(default=0),
        ),
    ]