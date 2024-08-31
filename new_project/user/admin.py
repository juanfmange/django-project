from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (
            None,{
                'fields': ('username', 'password')
            }
        ),
        ( 'Informacion Personal',{'fields': ('first_name', 'last_name', 'email')}),
        ('Otros',{'fields': ('is_active', 'is_superuser')}),
        ('Redes Sociales',{'fields': ('web_site', 'twitter',)}),
    )

