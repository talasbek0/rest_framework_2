# Generated by Django 4.2.7 on 2023-11-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PixelPulse', '0007_rename_number_of_days_customtourrequest_col_days_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
