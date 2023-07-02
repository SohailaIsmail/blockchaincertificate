# Generated by Django 4.1.6 on 2023-05-04 19:19

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studatapages', '0005_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('ID', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=13)),
            ],
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]