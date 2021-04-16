import pytest
from django.contrib.auth import get_user_model

__all__ = ['normal_user1', 'normal_user2', 'staff_user', 'admin_user', 'some_user']


User = get_user_model()


@pytest.fixture
def normal_user1():
    usr = User.objects.create_user('test1-user@example.com', 'passwd.1')
    usr.fullname = 'Private'
    usr.state = 'active'
    usr.save()
    return usr


@pytest.fixture
def normal_user2():
    usr = User.objects.create_user('test2-user@example.com', 'passwd.2')
    usr.fullname = 'Rico'
    usr.state = 'active'
    usr.save()
    return usr


@pytest.fixture
def some_user():
    usr = User.objects.create_user('some-user@example.com', 'passwd.3')
    usr.fullname = 'Julian'
    usr.state = 'active'
    usr.save()
    return usr


@pytest.fixture
def staff_user():
    usr = User.objects.create_user('staff@example.com', '11111111111')
    usr.fullname = 'Kowalski'
    usr.state = 'active'
    usr.is_staff = True

    usr.save()
    return usr


@pytest.fixture
def admin_user():
    usr = User.objects.create_user('admin@example.com', 'admin1')
    usr.fullname = 'Skipper'
    usr.state = 'active'
    usr.is_staff = True
    usr.is_superuser = True

    usr.save()
    return usr
