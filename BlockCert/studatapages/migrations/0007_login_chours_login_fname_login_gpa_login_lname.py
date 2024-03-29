# Generated by Django 4.1.6 on 2023-05-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studatapages', '0006_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='chours',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='fname',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='gpa',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='lname',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
