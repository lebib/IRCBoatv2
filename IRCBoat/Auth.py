#!/usr/bin/python3.4
#-*- coding: utf-8 -*-
from os import linesep
import hashlib
import fileinput

class User:
    separator = ' '

    def __init__(self, line):
        self.nick, self.password, self.level = line.strip().split(self.separator)

    def __str__(self):
        return self.separator.join([self.nick, self.password, self.level])

    def hash_password(self, password):
        pass

    def check_password(self, password):
        pass

    def __repr__(self, password):
        return '<{}.{} (nick: {}, level: {})>'.format(
            self.__class__.__module__,
            self.__class__.__qualname__,
            self.nick, self.level
        )

class UserList(dict):
    def __init__(self, source):
        self._source = source

        with open(source, 'r') as file:
            for user in map(User, file.readlines()):
                self[user.nick] = user

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
