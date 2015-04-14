# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from host_management.forms import RestaurantUserCreationForm, TableForm, PartyForm, AjaxReservationForm
from models import Table, Party
import datetime


def match(party):
    # estimated_time_list = []
    avg_total_reservation_time = Party.objects.filter(
        number_of_males=party.number_of_males,
        number_of_females=party.number_of_females,
        number_of_children=party.number_of_children,
        lunch=party.lunch,
        monday_to_thursday=party.monday_to_thursday,
        table__restaurant=party.table.restaurant,
        end_time__isnull=False
    ).extra(
        select={
            'avg_total_reservation_time': 'AVG("host_management_party"."end_time" - "host_management_party"."reservation_time")'
        }
    ).values('avg_total_reservation_time')[0]['avg_total_reservation_time']

    if avg_total_reservation_time:
        party.predicted_end_time = party.reservation_time + avg_total_reservation_time
        party.save()
    else:
        party.predicted_end_time = party.reservation_time + datetime.timedelta(0, 3600)
        party.save()


def home(request):
    return render(request, 'home.html')


@login_required()
@csrf_exempt
def profile(request):
    all_parties = Party.objects.all()
    for party in all_parties:
        party.predicted_end_time = party.reservation_time + datetime.timedelta(minutes=60)
        party.save()
        match(party)

    data = {
        'user': request.user,
        'tables': Table.objects.filter(restaurant__username=request.user),
        'parties': Party.objects.all(),
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
                                 restaurant=request.user)
            data = {
                'user': request.user,
                'tables': Table.objects.filter(restaurant__username=request.user)
            }
            return render(request, "profile.html", data)
        else:
            return render(request, "table_form.html")

    else:
        return render(request, "table_form.html", data)


@csrf_exempt
def party_form(request):
    data = {"party_form": PartyForm(restaurant=request.user)}
    if request.method == 'POST':
        form = PartyForm(request.POST, restaurant=request.user)
        if form.is_valid():
            Party.objects.create(party_name=form.cleaned_data['party_name'],
                                 number_of_males=form.cleaned_data['number_of_males'],
                                 number_of_females=form.cleaned_data['number_of_females'],
                                 number_of_children=form.cleaned_data['number_of_children'],
                                 lunch=form.cleaned_data['lunch'],
                                 monday_to_thursday=form.cleaned_data['monday_to_thursday'],
                                 reservation_time=form.cleaned_data['reservation_time'],
                                 table=form.cleaned_data['table'])
            return redirect("home")
        else:
            return HttpResponse("There was a problem with your entry, please try again")
    else:
        return render(request, "add_party.html", data)


def end_party(request, party_id):
    my_party = Party.objects.get(pk=party_id)
    my_party.end_time = datetime.datetime.now() - datetime.timedelta(0, 25200)
    my_party.save()
    return redirect("profile")

@csrf_exempt
def make_reservation_at_table(request, table_id):
    my_table = Table.objects.get(pk=table_id)
    data = {
        "table": my_table,
        "ajax_party_form": AjaxReservationForm()
    }
    if request.method == 'POST':
        form = AjaxReservationForm(request.POST)
        if form.is_valid():
            Party.objects.create(party_name=form.cleaned_data['party_name'],
                                 number_of_males=form.cleaned_data['number_of_males'],
                                 number_of_females=form.cleaned_data['number_of_females'],
                                 number_of_children=form.cleaned_data['number_of_children'],
                                 lunch=form.cleaned_data['lunch'],
                                 monday_to_thursday=form.cleaned_data['monday_to_thursday'],
                                 reservation_time=form.cleaned_data['reservation_time'],
                                 table=my_table)
            return redirect("home")
        else:
            return HttpResponse("There was a problem with your entry, please try again")
    else:
        return render_to_response("ajax_reservation.html", data)


def modal(request):
    return render("modal.html")