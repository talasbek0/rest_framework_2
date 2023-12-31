# Generated by Django 4.2.7 on 2023-11-23 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PixelPulse', '0006_customtourrequest_alter_review_tour'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customtourrequest',
            old_name='number_of_days',
            new_name='col_days',
        ),
        migrations.RenameField(
            model_name='customtourrequest',
            old_name='number_of_people',
            new_name='col_person',
        ),
        migrations.RenameField(
            model_name='customtourrequest',
            old_name='destinations',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='customtourrequest',
            old_name='accommodation_option',
            new_name='hotel_option',
        ),
        migrations.RenameField(
            model_name='customtourrequest',
            old_name='meal_option',
            new_name='meat_option',
        ),
    ]
