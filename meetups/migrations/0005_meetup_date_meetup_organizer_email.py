# Generated by Django 4.2.4 on 2023-08-28 06:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meetups", "0004_participant_meetup_participants"),
    ]

    operations = [
        migrations.AddField(
            model_name="meetup",
            name="date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="meetup",
            name="organizer_email",
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
