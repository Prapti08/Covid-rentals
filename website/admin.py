from django.contrib import admin
from .models import CustomUser, Room,UserContact,RoomImage, Reservation
from django.contrib.auth.admin import UserAdmin
from .forms import  SignUpForm,CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active','name','phno','date_of_birth',)
    list_filter = ('email', 'is_staff', 'is_active','name','phno','date_of_birth',)
    fieldsets = (
        (None, {'fields': ('email', 'password''name','phno','date_of_birth',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','name','phno','date_of_birth',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class RoomImageAdmin(admin.StackedInline):
    model = RoomImage

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines=[RoomImageAdmin]
    list_display = ('name','address','city','size','capacity','description','image','start_date','end_date')
    list_filter = ('status', 'start_date', 'end_date',)

    class meta:
        model=Room


@admin.register(RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(CustomUser)
admin.site.register(UserContact)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
      list_display = ('check_in', 'check_out', 'guest','room')
      ordering = ('check_in','check_out',)
      search_fields = ('guest', 'room')
