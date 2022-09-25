# Generated by Django 4.0.6 on 2022-09-25 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tienda', '0002_rename_image_producto_imagen'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'donacion',
                'verbose_name_plural': 'donaciones',
                'db_table': 'donaciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='LineaDonacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('donacion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donaciones.donacion')),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Linea Donacion',
                'verbose_name_plural': 'Linea Donaciones',
                'db_table': 'lineadonaciones',
                'ordering': ['id'],
            },
        ),
    ]
