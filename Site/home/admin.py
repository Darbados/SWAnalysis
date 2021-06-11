from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from home.models import AnalystUser


class AnalystUserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {
            'fields': ('email', 'password'),
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser'),
        }),
    )
    filter_horizontal = ()
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(AnalystUser, AnalystUserAdmin)
