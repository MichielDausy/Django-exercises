# Generated by Django 4.2 on 2024-01-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_rename_itel_price_item_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://static.wixstatic.com/media/bf242e_6133b4ae6a104cc2b50d70179f35efea~mv2.jpg/v1/fill/w_500,h_376,al_c,lg_1,q_80,enc_auto/food-placeholder.jpg', max_length=500),
        ),
    ]