#!/usr/bin/python3.4
#-*- coding: utf-8 -*-
from os import linesep
from passlib.hash import sha256_crypt
import csv

class User:
    separator = ','

    def __init__(self, line):
        self.login, password, self.level,self.nickname =line.strip().split(
            self.separator)
        self.password = self.hash_password(password)

    def __str__(self):
        return self.separator.join(
            [self.login, self.password, self.level, self.nickname]
        )

    def hash_password(self, password):
        """ string -> string
        Hash the given password using sha256 encryption.
        """
        return sha256_crypt.encrypt(password)

    def check_password(self, password):
        """ string -> bool
        Return truye if the given password is correct.
        """
        return self.password == hash_password(password)

    def __repr__(self):
        return '<{}.{} (login: {}, level: {})>'.format(
            self.__class__.__module__,
            self.__class__.__qualname__,
            self.login, self.level
        )

class UserList(dict):
    def __init__(self, source):
        self._source = source

        with open(source, newline='') as file:
            for user in map(User, file.readlines()):
                self[user.login] = user

    def save(self):
        with open(self._source, 'w') as file:
            for line in map(str, self.values()):
                file.write(line)
                file.write(linesep)

    def __repr__(self):
        return '<{}.{} (length: {}, source: {})>'.format(
            self.__class__.__module__,
            self.__class__.__qualname__,
            len(self), self._source
        )

class BOATAuth:
    def __init__(self, filename="USERS.csv"):
        self.filename = filename

    def add_user(self, login, password, level, nickname):
        """
        str, str, int, str ->
        Add a new user in the USER file at self.filename.
        Return something if the login is already used.
        """
        user_list = UserList(self.filename)
        user_list[login] = User(
            ','.join([login, password, str(level), nickname])
        )
        user_list.save()

    def delete_user(self, login):
        """ str ->
        Remove the user with the given login from the USER file.
        Do nothing if the user does not exist.
        """
        user_list = UserList(self.filename)
        del tel['login']
        user_list.save()

    def update_user(self, login, password=None, level=None, nickname=None):
        """ str, str, int, str ->
        Update the user with the given login from the USER file.
        The args with the None values will keep the old values.
        """
        if self.is_user(login):
            user_list = UserList(self.filename)
            old_user = user_list['login']
            if password is not None: old_user.password = password
            if level is not None: old_user.level = level
            if nickname is not None: old_user.nickname = nickname
            user_list[login] = User(
                old_user.separator.join([
                    old_user.login,
                    old_user.password,
                    old_user.level,
                    old_user.nickname])
            )
            user_list.save()

    def is_user(self, login):
        """ str -> bool
        Find if the user with the given login exist. Return true if yes.
        """
        user_list = UserList(self.filename)
        return login in user_list

    def is_user_connected(self, login):
        """ str -> bool
        Find if the user with the given login is connected. Return true if yes.
        """
        if self.get_user()
        user_list = UserList(self.filename)
        return user_list[login].nick != ''

    def get_user(self, login):
        """ str -> User
        Return the user with the given login. If he does not exist, return None
        instead.
        """
        user_list = UserList(self.filename)
        if self.is_user(login):
            return user_list[login]
        else:
            return None
