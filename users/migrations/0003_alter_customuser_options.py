# Generated by Django 5.0.6 on 2024-06-10 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_is_vendor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'CustomUser', 'verbose_name_plural': 'CustomUsers'},
        ),
    ]