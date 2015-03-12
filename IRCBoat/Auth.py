#!/usr/bin/python3.4
#-*- coding: utf-8 -*-
from os import linesep
from passlib.hash import sha256_crypt
import csv

class User:
    separator = ','

    def __init__(self, line):
        self.login, self.password, self.level,self.nickname =line.strip().split(
            self.separator)

    def __str__(self):
        return self.separator.join(
            [self.login, self.password, self.level, self.nickname]
        )

    def hash_password(self, password):
        return sha256_crypt.encrypt(password)

    def check_password(self, password):
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
        if self.is_user(login):
            return
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
        user_list[login] = ''
        user_list.save()

    def update_user(self, login, password=None, level=None, nickname=None):
        """ str, str, int, str ->
        Update the user with the given login from the USER file.
        The args with the None values will keep the old values.
        """
        pass

    def is_user(self, login):
        """ str -> bool
        Find if the user with the given login exist. Return true if yes.
        """
        return self.get_user(login) is not None

    def is_user_connected(self, login):
        """ str -> bool
        Find if the user with the given login is connected. Return true if yes.
        """
        user_list = UserList(self.filename)
        return user_list[login].nick is not None

    def get_user(self, login):
        """ str -> User
        Return the user with the given login. If he does not exist, return None
        instead.
        """
        user_list = UserList(self.filename)
        return user_list[login]
