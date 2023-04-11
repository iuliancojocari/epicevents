import pytest

from .models import User, Team

def test_exemple():
    assert 1 == 1


@pytest.mark.django_db
def test_my_user():
    team = Team.objects.create(name='test')

    assert str(team)