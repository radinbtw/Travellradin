# Generated by Django 3.1 on 2020-09-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='travel_mdl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('origin', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]