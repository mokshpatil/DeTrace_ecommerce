# Generated by Django 5.0.6 on 2024-06-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
