from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    meetups = [
        {"title": "meetup 1", "location": "USA", "slug": "meetup-1"},
        {"title": "meetup 2", "location": "Philippines", "slug": "meetup-2"},
    ]
    return render(
        request,
        "meetups/index.html",
        {
            "meetups": meetups,
            # "has_meetups": False,
            "has_meetups": True,
        },
    )
