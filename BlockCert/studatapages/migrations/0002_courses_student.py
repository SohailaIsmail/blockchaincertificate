# Generated by Django 4.1.7 on 2023-03-13 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studatapages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Code', models.CharField(max_length=50)),
                ('CRN', models.IntegerField(verbose_name=5)),
                ('hours', models.IntegerField(verbose_name=3)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField()),
                ('email', models.CharField(max_length=50, unique=True)),
                ('phone_num', models.PositiveSmallIntegerField()),
                ('college', models.CharField(max_length=30)),
                ('major', models.CharField(max_length=30)),
                ('current_year', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], verbose_name=3)),
                ('current_GPA', models.DecimalField(decimal_places=3, max_digits=7)),
                ('hours', models.PositiveSmallIntegerField()),
                ('img', models.ImageField(upload_to='photoes')),
                ('past_courses', models.ManyToManyField(to='studatapages.courses')),
            ],
        ),
    ]