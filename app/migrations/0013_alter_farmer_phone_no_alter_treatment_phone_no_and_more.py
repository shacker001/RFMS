# Generated by Django 4.1.2 on 2022-10-24 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_products_location_alter_products_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='phone_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='phone_no',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
