# Generated by Django 4.2 on 2024-01-22 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='itel_price',
            new_name='item_price',
        ),
    ]
