# Generated by Django 4.0.6 on 2022-09-25 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('politica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categorias',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='politica.categoriaprod'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='politica'),
        ),
    ]
