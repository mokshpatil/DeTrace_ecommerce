# Generated by Django 5.0.6 on 2024-06-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='add_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='wallet_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
