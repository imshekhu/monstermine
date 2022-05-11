from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # ...
    ordering = ('email',)
    list_display = ('email',)
    # fieldsets = (
    #     (None, {
    #         "fields": (
    #             ('email', 'first_name', 'last_name', 'is_staff',  'password', 'profit_today', 'profit_yesterday', 'amountmined', 
    #              'watcherlink', 'binance_profile_token', 'phone',)
                
    #         ),
    #     }),
    # )
    fieldsets = (
        (None, {"fields": (
                ('email', 'first_name', 'last_name', 'is_staff',  'password', 'profit_today', 'profit_yesterday', 'amountmined', 
                 'watcherlink', 'binance_profile_token',)
                
            ),}),
    )
    add_fieldsets =  (
        (None, {'fields': ('phone', 'password')}),
    )

admin.site.register(UserBase, CustomUserAdmin)