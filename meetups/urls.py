from django.urls import path

from . import views

# urls
urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>", views.meetup_detail, name="meetup-details"),
    path(
        "registration/success/<slug:organizer>",
        views.registration_success,
        name="reg-success",
    ),
]
