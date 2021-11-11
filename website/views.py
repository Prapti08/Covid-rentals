from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.forms import forms
from .forms import LoginForm,HostLoginForm, HostSignupForm,ContactForm,SignUpForm,RoomForm,ReservationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from allauth.account.views import LoginView
from .models import Room, Reservation
from django.views import generic


# Create your views here.


def login(request):
    """View function for login page of site."""
    submitted = False
    if request.method == 'POST':
         form = LoginForm(request.POST)
         if form.is_valid():
             cd = form.cleaned_data
             # assert False
             return HttpResponseRedirect('/contact?submitted=True')
    else:
         form = LoginForm()
         if 'submitted' in request.GET:
             submitted = True


    # Render the HTML template index.html with the data in the context variable
    return render(request, 'login2.html',{form: 'form'})


def home_view(request):
    # if this is a POST request we need to process the form data
    form=ContactForm(request.POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save(commit=True)
            # redirect to a new URL:
            return HttpResponseRedirect('/success/')
        else:
            print(form.errors)
            return HttpResponseRedirect('none')

    return render(request, "index6new.html",{form: 'form'})

def unsuccessful(request):
    return render(request,"unsuccessful.html")

def success(request):
    return render(request,"success.html")

def success1(request):
    return render(request,"success1.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('users:profile')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


class LocaLLoginView(LoginView):
    success_url = '/home'


def covidView(request):
    return render(request,"covidtracker.html")


@login_required
def roomRegistration_view(request):
    # if this is a POST request we need to process the form data
    form=RoomForm(request.POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RoomForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            #print(email)
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            size=form.cleaned_data['size']
            address=form.cleaned_data['address']
            capacity=form.cleaned_data['capacity']
            cost=form.cleaned_data['cost']
            city=form.cleaned_data['city']
            r = Room(size=size, address=address, capacity=capacity, cost=cost,city=city,email=request.user,name=name,description= description)
            r.save()
            print (form.__dict__)
            # redirect to a new URL:
            return HttpResponseRedirect('/room/success/')
        else:
            print(form.errors)
            print (form.__dict__)
            return HttpResponseRedirect('none')

    return render(request, "hostlogin.html",{form: 'form'})

@login_required
def delhi_view(request):
    house_list=Room.objects
    rooms=Room.objects.filter(city="Delhi")
    return render(request, 'rooms2.html', {'rooms':rooms})

@login_required
def mumbai_view(request):
    house_list=Room.objects
    rooms=Room.objects.filter(city="Mumbai")
    return render(request, 'rooms2.html', {'rooms':rooms})

@login_required
def pune_view(request):
    house_list=Room.objects
    rooms=Room.objects.filter(city="Pune")
    return render(request, 'rooms2.html', {'rooms':rooms})

@login_required
def bangalore_view(request):
    house_list=Room.objects
    rooms=Room.objects.filter(city="Bangalore")
    return render(request, 'rooms2.html', {'rooms':rooms})

@login_required
def kolkata_view(request):
    house_list=Room.objects
    rooms=Room.objects.filter(city="Kolkata")
    return render(request, 'rooms2.html', {'rooms':rooms})

def dashboard_view(request):
    #reservations=Reservation.objects(filter(guest=request.user))
    # if this is a POST request we need to process the form data
    form=ContactForm(request.POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save(commit=True)
            # redirect to a new URL:
            return HttpResponseRedirect('/success/')
        else:
            print(form.errors)
            return HttpResponseRedirect('none')

    return render(request, "dashboard4.html")

from django.shortcuts import redirect
from django.utils.translation import gettext as _

def confirm(request, pk = None):
    if request.method == 'POST':
        if pk:
            invalid_dates = False
            #get the room
            room = Room.objects.get(pk = pk)
            guest_id = request.user
            check_in = request.session['check_in']
            check_out = request.session['check_out']

            # check whether the dates are valid
            # case 1: a room is booked before the check_in date, and checks out after the requested check_in date
            case_1 = Reservation.objects.filter(room=room, check_in__lte=check_in, check_out__gte=check_in).exists()

            # case 2: a room is booked before the requested check_out date and check_out date is after requested check_out date
            case_2 = Reservation.objects.filter(room=room, check_in__lte=check_out, check_out__gte=check_out).exists()

            case_3 = Reservation.objects.filter(room=room, check_in__gte=check_in, check_out__lte=check_out).exists()


            # if either of these is true, abort and render the error
            if case_1 or case_2 or case_3:
                  return render(request, "system/reserve.html", {"errors": "This room is not available on your selected dates"})

            # dates are valid
            reservation=Reservation(
            check_in = check_in,
            check_out = check_out,
            room_id = room.id,
            guest_id = guest_id.id
            )

            reservation.save()

            #redirect to success page (need to define this as a separate view)
            return redirect("/success1")

import datetime
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.core.exceptions import ValidationError

class RoomBookingView(FormMixin,DetailView):
    model = Room
    form_class = ReservationForm
    template_name = 'room_detail_new2.html'


    def get_context_data(self, **kwargs):
        context = super(RoomBookingView, self).get_context_data(**kwargs)
        context['form'] = ReservationForm(initial={'post': self.object})
        return context

    def get_success_url(self):
        return reverse('success1')


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print (form.errors)
            return self.form_invalid(form)

    def form_valid(self, form):
        check_in=form.cleaned_data['check_in']
        check_out=form.cleaned_data['check_out']
        guest_id=self.request.user
        room_id = self.kwargs['pk']
        room = Room.objects.get(pk =self.kwargs['pk'])
        if check_in < datetime.date.today() or check_out < datetime.date.today():
            raise ValidationError(_('Invalid value'), code='invalid')

        case_1 = Reservation.objects.filter(room=room, check_in__lte=check_in, check_out__gte=check_in).exists()

        # case 2: a room is booked before the requested check_out date and check_out date is after requested check_out date
        case_2 = Reservation.objects.filter(room=room, check_in__lte=check_out, check_out__gte=check_out).exists()


        case_3 = Reservation.objects.filter(room=room, check_in__gte=check_in, check_out__lte=check_out).exists()



        # if either of these is true, abort and render the error
        if case_1 or case_2 or case_3:
              return reverse('unsuccessful')

        #room_id = room.name
        else:
           r = Reservation(check_in = check_in, check_out=check_out, guest_id=guest_id,room_id=room_id)
           r.save()
           #room = Room.objects.get(pk = pk)

        return super(RoomBookingView, self).form_valid(form)




        form.save()
        return super(RoomBookingView, self).form_valid(form)



def test_view(request):
    return render(request,'covidtracker.html')
