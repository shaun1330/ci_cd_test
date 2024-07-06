from django.test import TestCase

# Create your tests here.

import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create(user):
  assert User.objects.count() == 1
  assert User.objects.get(username='john').email == 'lennon@thebeatles.com'


def test_hello_world():
    assert 1 == 1