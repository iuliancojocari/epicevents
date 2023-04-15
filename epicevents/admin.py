from django.contrib import admin
from .models import Client, Contract, Event


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "company_name",
        "is_client",
        "sales_contact",
    ]
    fieldsets = [
        (
            "Client",
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "company_name",
                    "email",
                    "phone",
                    "mobile",
                    "is_client",
                    "sales_contact",
                ]
            },
        ),
        ("About", {"fields": ["date_created", "date_updated"]}),
    ]
    readonly_fields = ["date_created", "date_updated"]
    list_filter = ["is_client"]
    search_fields = [
        "first_name",
        "last_name",
        "company_name",
        "email",
        "sales_contact",
    ]
    ordering = ["is_client"]


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = [
        "client",
        "status",
        "amount",
        "payment_due",
        "sales_contact",
    ]
    fieldsets = [
        (
            "Contract",
            {"fields": ["client", "status", "amount", "payment_due", "sales_contact"]},
        ),
        ("About", {"fields": ["date_created", "date_updated"]}),
    ]
    readonly_fields = ["date_created", "date_updated"]
    list_filter = ["status"]
    search_fields = ["client", "sales_contact", "payment_due"]
    ordering = ["status"]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        "client_contract",
        "attendees",
        "event_date",
        "event_status",
        "support_contact",
    ]
    fieldsets = [
        (
            "Event",
            {
                "fields": [
                    "client_contract",
                    "attendees",
                    "event_date",
                    "event_status",
                    "notes",
                    "support_contact",
                ]
            },
        ),
        ("About", {"fields": ["date_created", "date_updated"]}),
    ]
    readonly_fields = ["date_created", "date_updated"]
    list_filter = ["event_status", "attendees"]
    search_fields = [
        "client_contract",
        "support_contact",
    ]
    ordering = ["event_status"]
