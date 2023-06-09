# Generated by Django 4.2 on 2023-04-12 13:28

from django.db import migrations
from users.models import MANAGEMENT, SALES, SUPPORT


def create_teams(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    teams = apps.get_model("users", "Team")
    for name in [MANAGEMENT, SALES, SUPPORT]:
        teams.objects.using(db_alias).create(name=name)


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_teams)]
