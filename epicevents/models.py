from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Client(models.Model):
    first_name = models.CharField(_("First name"), max_length=25, blank=False)
    last_name = models.CharField(_("Last name"), max_length=25, blank=False)
    email = models.CharField(
        _("Email address"), max_length=100, unique=True, blank=False
    )
    phone = models.CharField(_("Phone"), max_length=20, blank=True)
    mobile = models.CharField(_("Mobile"), max_length=20, blank=True)
    company_name = models.CharField(_("Company name"), max_length=250, blank=False)
    is_client = models.BooleanField(_("Is client ?"), default=False)
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        limit_choices_to={"team_id": 2},
        related_name="client_sales_contact",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contract(models.Model):
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True)
    status = models.BooleanField(_("Is signed"), default=False)
    amount = models.FloatField(_("Amount"), blank=False)
    payment_due = models.DateField(_("Payment due"), blank=False)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        limit_choices_to={"team_id": 2},
        related_name="contract_sales_contact",
    )
    client = models.ForeignKey(
        to=Client, on_delete=models.CASCADE, related_name="contract"
    )

    def __str__(self):
        return f"{self.client}"


class Event(models.Model):
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True)
    event_status = models.BooleanField(_("Event status"), default=False)
    attendees = models.IntegerField(_("Attendees"), validators=[MinValueValidator(1)])
    event_date = models.DateField(_("Event date"), blank=False)
    notes = models.TextField(_("Event notes"), blank=True)
    client_contract = models.ForeignKey(
        to=Contract, on_delete=models.CASCADE, related_name="event"
    )
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        limit_choices_to={"team_id": 3},
        related_name="event_support_contact",
    )

    def __str__(self):
        return f"{self.client_contract.client}"
