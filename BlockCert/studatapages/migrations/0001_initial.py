# Generated by Django 4.1.7 on 2023-03-13 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=13)),
            ],
        ),
    ]
