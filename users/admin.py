from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    list_display = ["first_name", "last_name", "email", "team", "is_staff"]
    list_filter = ["team", "is_active"]
    fieldsets = [
        ("Login", {"fields": ["email", "password"]}),
        ("User", {"fields": ["first_name", "last_name", "phone", "mobile"]}),
        ("Permissions", {"fields": ["team"]}),
    ]

    add_fieldsets = [
        (
            "User Information",
            {
                "fields": (
                    "email",
                    "password",
                    "confirm_password",
                    "first_name",
                    "last_name",
                    "phone",
                    "mobile",
                    "team",
                )
            },
        )
    ]

    search_fields = ["email"]
    ordering = ["team"]
