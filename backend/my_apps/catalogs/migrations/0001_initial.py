# Generated by Django 4.2.7 on 2023-11-19 23:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MaxLengthValidator(20), django.core.validators.RegexValidator('^\\w[\\w\\d]{1,19}$', 'Name is a string of characters + digits')])),
            ],
            options={
                'db_table': 'catalog_car_brands',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='LocalitiesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale_id', models.PositiveIntegerField(unique=True)),
                ('type', models.CharField(max_length=20)),
                ('name', models.JSONField()),
                ('public_name', models.JSONField()),
                ('post_code', models.JSONField()),
                ('katottg', models.CharField(max_length=20)),
                ('koatuu', models.CharField(max_length=10)),
                ('lng', models.FloatField(blank=True)),
                ('lat', models.FloatField(blank=True)),
                ('parent_id', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'localities',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CarBrandModelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MaxLengthValidator(20), django.core.validators.RegexValidator('^\\w[\\w\\d]{1,19}$', 'Name is a string of characters + digits')])),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_brand', to='catalogs.carbrandmodel')),
            ],
            options={
                'db_table': 'catalog_car_brand_models',
                'ordering': ['id'],
            },
        ),
    ]
