# Generated by Django 4.2.4 on 2023-08-29 03:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meetups", "0005_meetup_date_meetup_organizer_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meetup",
            name="participants",
            field=models.ManyToManyField(blank=True, to="meetups.participant"),
        ),
        migrations.AlterField(
            model_name="participant",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
