import pytest

from .models import User, Team


class TestTeamModel:
    """
    Test Team Model : Creation, Deletion
    """

    @pytest.mark.django_db
    def test_add_new_team(self):
        data = {"name": "Test team"}
        team = Team.objects.create(name=data["name"])

        assert str(team) == "Test team"
        assert Team.objects.count() == 1

    @pytest.mark.django_db
    def test_delete_team(self):
        data = {"name": "Test team"}

        Team.objects.create(name=data["name"])
        assert Team.objects.count() == 1

        team = Team.objects.get(name="Test team")
        team.delete()
        assert Team.objects.count() == 0


class TestUserModel:
    """
    Test User Model : Creation, Deletion
    """

    @pytest.mark.django_db
    def test_create_user_with_null_team(self):
        user = User.objects.create(
            first_name="First Name",
            last_name="Last Name",
            email="email@exemple.com",
            phone="0123456789",
            mobile="0123456789",
            team=Team().save(),
        )

        assert User.objects.count() == 1
        assert str(user.first_name) == "First Name"
        assert str(user.last_name) == "Last Name"
        assert str(user.email) == "email@exemple.com"
        assert str(user.phone) == "0123456789"
        assert str(user.mobile) == "0123456789"
        assert user.team == None
        assert str(user) == "First Name Last Name | email@exemple.com"

    @pytest.mark.django_db
    def test_create_user_with_new_valid_team(self):
        User.objects.create(
            id=10,
            first_name="First Name",
            last_name="Last Name",
            email="email@exemple.com",
            phone="0123456789",
            mobile="0123456789",
            team=Team.objects.create(name="Sales"),
        )

        assert User.objects.count() == 1
        assert User.objects.get(id=10).first_name == "First Name"
        assert User.objects.get(id=10).last_name == "Last Name"
        assert User.objects.get(id=10).email == "email@exemple.com"
        assert User.objects.get(id=10).phone == "0123456789"
        assert User.objects.get(id=10).mobile == "0123456789"
        assert User.objects.get(id=10).team == Team.objects.get(name="Sales")
