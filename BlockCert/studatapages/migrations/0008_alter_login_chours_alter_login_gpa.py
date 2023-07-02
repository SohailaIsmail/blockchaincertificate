# Generated by Django 4.1.6 on 2023-05-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studatapages', '0007_login_chours_login_fname_login_gpa_login_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='chours',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='login',
            name='gpa',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
