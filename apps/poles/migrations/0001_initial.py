# Generated by Django 4.0.5 on 2022-07-04 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('inches', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('purchased_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout', models.DateTimeField()),
                ('due', models.DateTimeField()),
                ('returned', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comment', models.TextField(max_length=300)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='poles.customer')),
                ('pole', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='poles.pole')),
            ],
        ),
    ]
