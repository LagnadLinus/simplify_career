# Generated by Django 5.1.1 on 2024-09-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime_rate', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EducationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_level', models.CharField(max_length=255)),
                ('family_income', models.FloatField()),
                ('year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IncomeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_income', models.FloatField()),
                ('year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MentalHealthData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mental_health_issues', models.BooleanField()),
                ('support_needed', models.BooleanField()),
                ('year', models.PositiveIntegerField()),
            ],
        ),
    ]
