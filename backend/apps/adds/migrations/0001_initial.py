# Generated by Django 4.2.7 on 2023-11-23 12:05

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.PositiveSmallIntegerField()),
                ('price', models.FloatField()),
                ('currency', models.CharField(choices=[('UAH', 'UAH'), ('USD', 'USD'), ('EUR', 'EUR')], default='UAH', max_length=3)),
                ('description', models.TextField(max_length=300, validators=[django.core.validators.MaxLengthValidator(300, 'Total length must not exceed 300 symbols')])),
                ('brand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='catalogs.carbrandmodel')),
                ('model', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='brand_models', to='catalogs.carbrandmodelmodel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'adds',
                'ordering': ['id'],
            },
        ),
    ]
