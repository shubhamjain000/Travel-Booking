from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, TravelOption

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["phone", "address"]
        widgets = {
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. +91-98765-43210"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Address"}),
        }

class TravelFilterForm(forms.Form):
    type = forms.ChoiceField(
        choices=[("", "Any Type")] + TravelOption.TYPE_CHOICES,
        required=False,
        widget=forms.Select(attrs={"class": "form-select"})
    )
    source = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Delhi"}))
    destination = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Mumbai"}))
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}))

class BookingForm(forms.Form):
    num_seats = forms.IntegerField(min_value=1, label="Number of Seats",
                                   widget=forms.NumberInput(attrs={"class": "form-control"}))
