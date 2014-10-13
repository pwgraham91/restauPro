# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from host_management.forms import RestaurantUserCreationForm, TableForm, PartyForm
from models import Table, Party
from datetime import timedelta


def match(party):
    estimation_list = []
    for this_party in Party.objects.all():
        if party.number_of_males == this_party.number_of_males:
            if party.number_of_females == this_party.number_of_females:
                if party.number_of_children == this_party.number_of_children:
                    if (party.lunch and this_party.lunch) or (party.lunch == False and this_party.lunch == False):
                        pass
                    # elif party.dinner and this_party.dinner:


def home(request):
    return render(request, 'home.html')


@login_required()
def profile(request):
    all_parties = Party.objects.all()
    for party in all_parties:
        party.predicted_end_time = party.reservation_time + timedelta(minutes=60)
        party.save()
        match(party)
    my_tables = Table.objects.filter(premise__username=request.user)
    sorted_tables = []
    for table in my_tables:
        sorted_tables.append(table)
    sorted_tables.sort(key=lambda x: x.table_name, reverse=False)
    data = {
        'user': request.user,
        'tables': sorted_tables,
        'parties': Party.objects.all()
    }
    return render(request, 'profile.html', data)


def register(request):
    if request.method == 'POST':
        form = RestaurantUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            if form.save():
                return redirect("profile")
    else:
        form = RestaurantUserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


def table_form(request):
    data = {"table_form": TableForm()}
    if request.method == 'POST':
        form = TableForm(request.POST, request.FILES)
        if form.is_valid():
            Table.objects.create(table_name=form.cleaned_data['table_name'],
                                 seats=form.cleaned_data['seats'],
                                 x_position=form.cleaned_data['x_position'],
                                 y_position=form.cleaned_data['y_position'],
                                 premise=request.user)
            data = {
                'user': request.user,
                'tables': Table.objects.filter(premise__username=request.user)
            }
            return render(request, "profile.html", data)
        else:
            return render(request, "table_form.html")

    else:
        return render(request, "table_form.html", data)


def party_form(request):
    data = {"party_form": PartyForm(restaurant=request.user)}
    if request.method == 'POST':
        form = PartyForm(request.POST, restaurant=request.user)
        print form

        if form.is_valid():
            Party.objects.create(party_name=form.cleaned_data['party_name'],
                                 number_of_males=form.cleaned_data['number_of_males'],
                                 number_of_females=form.cleaned_data['number_of_females'],
                                 number_of_children=form.cleaned_data['number_of_children'],
                                 lunch=form.cleaned_data['lunch'],
                                 monday_to_thursday=form.cleaned_data['monday_to_thursday'],
                                 reservation_time=form.cleaned_data['reservation_time'],
                                 seated_table=form.cleaned_data['seated_table'])
            return render(request, "home.html")
        else:
            return HttpResponse("There was a problem with your entry, please try again")
    else:
        return render(request, "add_party.html", data)