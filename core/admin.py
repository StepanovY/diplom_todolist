from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from core.models import User


@admin.register(User)
class BaseUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    readonly_fields = ('last_login', 'date_joined',)
    fieldsets = (
        (
            None,
            {'fields': ('username', 'password')}
        ),
        (
            'Personal info',
            {'fields': ('first_name', 'last_name', 'email')}
        ),
        (
            'Permissions',
            {'fields': ('is_active', 'is_superuser', 'is_staff')}
        ),
        (
            'Other info',
            {'fields': ('last_login', 'date_joined')}
        ),
    )


admin.site.unregister(Group)
