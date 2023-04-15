# Generated by Django 4.2 on 2023-04-15 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=25, verbose_name="First name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=25, verbose_name="Last name"),
                ),
                (
                    "email",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Email address"
                    ),
                ),
                (
                    "phone",
                    models.CharField(blank=True, max_length=20, verbose_name="Phone"),
                ),
                (
                    "mobile",
                    models.CharField(blank=True, max_length=20, verbose_name="Mobile"),
                ),
                (
                    "company_name",
                    models.CharField(max_length=250, verbose_name="Company name"),
                ),
                ("is_client", models.BooleanField(verbose_name="Is client ?")),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date created"
                    ),
                ),
                (
                    "date_updated",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date updated"
                    ),
                ),
                (
                    "sales_contact",
                    models.ForeignKey(
                        limit_choices_to={"team_id": "Sales"},
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
