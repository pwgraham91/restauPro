# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from host_management.forms import RestaurantUserCreationForm, TableForm, PartyForm
from models import Restaurant, Table, Party

def home(request):
    return render(request, 'home.html')

@login_required()
def profile(request):
    data = {
        'user': request.user
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
            return render(request, "profile.html")
        else:
            return render(request, "table_form.html")

    else:
        return render(request, "car_form.html", data)