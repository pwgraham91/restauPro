__author__ = 'GoldenGate'
from django.contrib.auth.forms import UserCreationForm
from host_management.models import Restaurant, Table, Party
from django import forms


class RestaurantUserCreationForm(UserCreationForm):
    class Meta:
        model = Restaurant
        fields = ("username", "restaurant_name" "password1", "password2", "email")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Restaurant.objects.get(username=username)
        except Restaurant.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

class TableForm(forms.Form):
    table_name = forms.CharField(label="example: 103 (do not put 'table 103' just '103'")
    seats = forms.IntegerField(label="number of maximum available seats at the table")

class PartyForm(forms.Form):
    party_name = forms.CharField(label="Enter this if you know the name of the party so you can save their data")
    number_of_males = forms.IntegerField(label="Number of adult males in party")
    number_of_females = forms.IntegerField(label="Number of adult females in party")
    number_of_children = forms.IntegerField(label="Number of children in party")
    lunch = forms.BooleanField(label="Check true for lunch or false for dinner")
    weekday = forms.BooleanField(label="Check true for Monday through Thursday or false for Friday through Sunday")
    reservation_time = forms.DateTimeField(label="Reservation time")