# Generated by Django 4.1.2 on 2022-10-17 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_farmers_alter_treatment_disease_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treatment',
            old_name='describe',
            new_name='Description',
        ),
    ]
