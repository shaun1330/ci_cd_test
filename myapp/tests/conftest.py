import pytest


@pytest.fixture
def user(db):
    from django.contrib.auth.models import User
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    yield
    User.objects.all().delete()


