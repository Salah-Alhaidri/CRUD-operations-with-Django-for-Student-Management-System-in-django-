# Generated by Django 5.1.2 on 2024-11-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecordModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('student_age', models.PositiveIntegerField()),
                ('student_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('enrollment_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
