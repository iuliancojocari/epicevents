# Generated by Django 4.2 on 2023-04-15 08:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("epicevents", "0003_alter_contract_payment_due"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="sales_contact",
            field=models.ForeignKey(
                limit_choices_to={"team_id": 2},
                on_delete=django.db.models.deletion.PROTECT,
                related_name="contract_sales_contact",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Event",
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
                    "event_status",
                    models.BooleanField(default=False, verbose_name="Event status"),
                ),
                (
                    "attendees",
                    models.IntegerField(
                        validators=[django.core.validators.MinLengthValidator(0)],
                        verbose_name="Attendees",
                    ),
                ),
                ("event_date", models.DateField(verbose_name="Event date")),
                ("notes", models.TextField(blank=True, verbose_name="Event notes")),
                (
                    "contract",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contract",
                        to="epicevents.contract",
                    ),
                ),
                (
                    "support_contact",
                    models.ForeignKey(
                        limit_choices_to={"team_id": 3},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="event_support_contact",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]