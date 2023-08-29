from django.db import models


# Create your models here.
class Location(models.Model):
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.city}, {self.country}"


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=240)
    slug = models.SlugField(unique=True, db_index=True)
    organizer_email = models.EmailField(null=True)
    date = models.DateField(null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images", null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    participants = models.ManyToManyField(Participant, blank=True)

    def __str__(self):
        return self.title
