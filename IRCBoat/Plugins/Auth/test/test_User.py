import pytest
import os
from passlib.hash import sha256_crypt
from IRCBoat.Plugins.Auth.User import User, UserList


@pytest.fixture
def init_user():
    user = "T"
    password = "T"
    level = "1"
    nickname = "T"
    host = "T"
    return User("{},{},{},{},{}".format(
                user,
                User.hash_password(password),
                level, nickname, host
                ))


@pytest.yield_fixture
def init_user_list():
    f = open('USERS.csv', 'w')
    f.write(str(init_user()))
    f.close()
    yield(UserList('USERS.csv'))
    os.remove('USERS.csv')

###############################################################################


def test_user_init():
    user = init_user()
    assert user.login == "T"
    assert user.level == "1"
    assert user.nickname == "T"
    assert user.host == "T"


def test_user_hash_password():
    user = init_user()
    assert sha256_crypt.verify("T", user.password)


def test_user_check_password():
    user = init_user()
    assert user.check_password("T")

###############################################################################


def test_user_list_init(init_user_list):
    userList = init_user_list
    assert len(userList) == 1


def test_user_list_save(init_user_list):
    userList = init_user_list
    user = init_user()
    user.login = "T2"
    userList["T2"] = user
    userList.save()
    userList = UserList('USERS.csv')
    assert len(userList) == 2
