__author__ = 'GoldenGate'
from django.contrib.auth.forms import UserCreationForm
from host_management.models import Restaurant, Table, Party
from django import forms


class RestaurantUserCreationForm(UserCreationForm):
    class Meta:
        model = Restaurant
        fields = ("username", "restaurant_name", "password1", "password2", "email")

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
    table_name = forms.CharField(label="Table Name: example: 103 (do not put 'table 103' just '103')")
    seats = forms.IntegerField(label="number of maximum available seats at the table")
    x_position = forms.IntegerField(label="x grid position of the table")
    y_position = forms.IntegerField(label="y grid position of the table")

class PartyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        restaurant = kwargs.pop('restaurant', None)
        super(PartyForm, self).__init__(*args, **kwargs)
        self.fields['seated_table'] = forms.ModelChoiceField(Table.objects.filter(premise=restaurant))
        self.fields['party_name'].label = "Party Name"
    class Meta:
        model = Party
        fields = ("party_name", "number_of_males", "number_of_females",
                  "number_of_children", "lunch", "monday_to_thursday",
                  "reservation_time", "seated_table")

class AjaxReservationForm(forms.Form):
    party_name = forms.CharField(label="Enter this if you know the name of the party so you can save their data")
    number_of_males = forms.IntegerField()
    number_of_females = forms.IntegerField()
    number_of_children = forms.IntegerField()
    lunch = forms.BooleanField(label="check true for lunch or false for dinner")
    monday_to_thursday = forms.BooleanField(label="check true for Monday to Thursday or false for Friday to Sunday")
    reservation_time = forms.DateTimeField()