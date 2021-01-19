from django import forms
import datetime
from .models import CustomUser,Room,UserContact, Reservation
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm,LoginForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('__all__')

class CustomLoginForm(LoginForm):
   def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'red-border'
            })

class CustomSignupForm(SignupForm):
   def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields["date_of_birth"] = forms.DateTimeField(label='Date of Birth', required=True)
        self.fields["phno"] = forms.CharField(label='Phone Number', max_length=30)



class HostLoginForm(forms.ModelForm):
      class Meta:
          model = CustomUser
          fields = '__all__'
          exclude=['name','date_of_birth','phno']

class HostSignupForm(forms.ModelForm):
   class Meta:
       model = CustomUser
       fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = UserContact
        fields = '__all__'

CITY_CHOICES= (
    ('Pune', 'Pune'),
    ('Mumbai', 'Mumbai'),
    ('Bangalore', 'Bangalore'),
    ('Kolkata', 'Kolkata'),
    ('Delhi', 'Delhi'),
    )

class RoomForm(forms.ModelForm):
   city=forms.ChoiceField(choices=CITY_CHOICES)
   class Meta:
       model = Room
       fields = ['size','address','capacity','cost','city','name','description']


class ReservationForm(forms.ModelForm):
   class Meta:
       model = Reservation
       fields = ('__all__')
       exclude = ['guest','room']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class LoginForm(forms.Form):
    """user login form"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=CustomUser
        fields='__all__'
