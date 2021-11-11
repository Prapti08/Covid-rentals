from django.db import models
from django import forms
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid

# Create your models here.
from .managers import CustomUserManager
from django.urls import reverse # Used to generate URLs by reversing the URL patterns\

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, db_index=True, primary_key=True)
    name = models.CharField(max_length=200,blank=False)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    phno = models.TextField(max_length=10)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phno','date_of_birth']

    objects = CustomUserManager()

    def __str__(self):
        return self.email



CITY_CHOICES= [
    ('Pune', 'Pune'),
    ('Mumbai', 'Mumbai'),
    ('Bangalore', 'Bangalore'),
    ('Kolkata', 'Kolkata'),
    ('Delhi', 'Delhi'),
    ]

class Room(models.Model):
    """Model representing a room."""

    HOUSE_STATUS=(
        ('r', 'Reserved'),
        ('a', 'Available'),
        ('m', 'On maintainence'),
     )



    size = models.IntegerField(blank=False, null = False)
    address = models.TextField(blank=False, null = False)
    capacity = models.TextField(blank=False, null = False)
    city=models.CharField(choices=CITY_CHOICES,max_length=10,default="Pune")
    cost = models.TextField(blank=False, null = False)
    name = models.CharField(max_length=250,default = "Room name")
    description = models.TextField(max_length=800, default="Sample description")
    email = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',default='images/default_room.jpg',blank=True)
    start_date = models.DateTimeField(default=timezone.now,blank=True)
    end_date = models.DateTimeField(default=timezone.now,blank=True)
    status = models.CharField(
        max_length=1,
        choices=HOUSE_STATUS,
        blank=True,
        default='a',
        help_text='Room availability',
    )
    class Meta:
        ordering = ['name']




    def __str__(self):
        """String for representing the Model object."""
        return self.name


    def get_absolute_url(self):
        """Returns the url to access a detail record for this Room."""
        return reverse('room-detail', args=[str(self.id)])

class RoomImage(models.Model):
    room = models.ForeignKey(Room, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/',default='images/default_room.jpg')
    def __str__(self):
        return self.room.title

class UserContact(models.Model):

    def display_genre(self):
        """Create a string for the user. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Contact'

    mail = models.CharField(max_length=200,blank=False)
    message = models.CharField(max_length=200,blank=False)


    def __str__(self):
        """String for representing the Model object."""
        return self.mail

    def get_absolute_url(self):
        """Returns the url to access a detail record for this owner."""
        return reverse('customer-detail', args=[str(self.id)])

class Reservation(models.Model):
    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField()
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    guest = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    class Meta:
       verbose_name = 'Reservation'
       verbose_name_plural = 'Reservations'
