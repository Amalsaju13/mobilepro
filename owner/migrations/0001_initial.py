# Generated by Django 4.0.2 on 2022-03-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_name', models.CharField(max_length=120, unique=True)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('specification', models.CharField(max_length=350)),
                ('camera', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=50)),
                ('storage', models.CharField(max_length=40)),
            ],
        ),
    ]