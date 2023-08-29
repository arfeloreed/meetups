from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import RegistrationForm
from .models import Meetup, Participant


# Create your views here.
def index(request):
    meetups = Meetup.objects.all()

    return render(
        request,
        "meetups/index.html",
        {
            "meetups": meetups,
        },
    )


def meetup_detail(request, slug):
    try:
        selected_meetup = Meetup.objects.get(slug=slug)

        if request.method == "GET":
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)

            if registration_form.is_valid():
                # commented out because I am not using a modelForm
                # participant = registration_form.save()
                # connect the registered participant to the related meetup field
                # selected_meetup.participants.add(participant)

                # using the django normal form creation and checking - creating a participant
                user_email = registration_form.cleaned_data["email"]
                # participant, was_created = Participant.objects.get_or_create(email=user_email)
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return HttpResponseRedirect(reverse("reg-success", args=[slug]))

        return render(
            request,
            "meetups/meetup-detail.html",
            {
                "meetup": selected_meetup,
                "has_meetup": True,
                "form": registration_form,
            },
        )
    except Exception as exc:
        return render(
            request,
            "meetups/meetup-detail.html",
            {
                "has_meetup": False,
            },
        )


def registration_success(request, organizer):
    meetup = Meetup.objects.get(slug=organizer)
    return render(
        request,
        "meetups/registration-success.html",
        {
            "organizer": meetup.organizer_email,
        },
    )
