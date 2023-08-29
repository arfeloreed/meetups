from django import forms

# from .models import Participant

# form models below
# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = [
#             "email",
#         ]


# since where not using form.save() directly, we can use a normal django form creation
class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Your Email")
