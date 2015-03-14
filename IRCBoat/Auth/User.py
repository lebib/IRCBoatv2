#!/usr/bin/python3.4
#-*- coding: utf-8 -*-

from os import linesep
from passlib.hash import sha256_crypt
import csv

class User:
    separator = ','

    def __init__(self, line):
        self.login, password, self.level, self.nickname = line.strip().split(
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
