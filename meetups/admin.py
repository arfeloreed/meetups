from django.contrib import admin

from .models import Location, Meetup, Participant


# manipulate the display
class MeetupAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("location", "date")


# Register your models here.
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
