# Generated by Django 4.0.6 on 2022-09-24 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='image',
            new_name='imagen',
        ),
    ]
