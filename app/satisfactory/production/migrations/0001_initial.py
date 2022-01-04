# Generated by Django 4.0 on 2022-01-03 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(max_length=32, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('process_time', models.DurationField()),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='production.factory')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='used_by', to='production.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProducedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('production_time', models.DurationField()),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produced_products', to='production.factory')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produced_by', to='production.product')),
            ],
        ),
    ]
