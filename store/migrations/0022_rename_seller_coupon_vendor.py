# Generated by Django 5.0.6 on 2024-06-18 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_coupon_code_coupon_is_active_alter_coupon_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='seller',
            new_name='vendor',
        ),
    ]