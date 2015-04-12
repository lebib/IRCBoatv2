import pytest
import os
from IRCBoat.Plugins.Auth.Auth import Auth
from IRCBoat.Plugins.Auth.User import UserList


@pytest.yield_fixture
def init_auth():
    f = open('USERS.csv', 'w')
    f.close()
    yield(Auth('USERS.csv'))
    os.remove('USERS.csv')


def test_auth_add_user(init_auth):
    auth = init_auth
    auth.add_user('T', 'T', 1)
    assert len(UserList('USERS.csv')) == 1
    # need to check if all the datas are okay


def test_auth_delete_user(init_auth):
    auth = init_auth
    auth.add_user('T', 'T', 1)
    auth.delete_user('T')
    assert len(UserList('USERS.csv')) == 0


def test_auth_update_user(init_auth):
    auth = init_auth
    auth.add_user('T', 'T', 1)
    auth.update_user('T', 'T', 1, 'T', 'T')
    user_list = UserList('USERS.csv')
    assert user_list["T"].host == "T"
    assert user_list["T"].nickname == "T"


def test_auth_is_user(init_auth):
    auth = init_auth
    auth.add_user("T", "T", 1)
    assert auth.is_user("T")


def test_auth_is_user_connected(init_auth):
    auth = init_auth
    auth.add_user("T", "T", 1, "T", "T")
    assert auth.is_user_connected("T")


def test_auth_get_user(init_auth):
    auth = init_auth
    auth.add_user("T", "T", 1)
    assert int(auth.get_user("T").level) == 1
