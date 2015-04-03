from os import linesep
from passlib.hash import sha256_crypt
import csv

class User:
    """ User are cosidered as entries inside a csv file manipulated by UserList.

    :param line: the line who'll be parsed.
    :type line: str

    The content of line is based on : ``LOGIN,PASSWORD,LEVEL,NICKNAME,HOST,``

    The hashing, salting and encrypting is made by sha256_crypt from the passlib
    library.

    :Example: ``"myLogin,myPassword,0,myCurrentNickname,myCurrentHost"``
    """
    separator = ','

    def __init__(self, line):
        data = line.strip().split(self.separator)
        self.login, self.password, self.level, self.nickname, self.host = data

    def __str__(self):
        return self.separator.join(
            [self.login, self.password, self.level, self.nickname, self.host]
        )

    @staticmethod
    def hash_password(password):
        """ Make an hash out of the password.

        :param password: password to hash
        :type password: str
        :return: Hash of the password
        :rtype: str
        """
        return sha256_crypt.encrypt(password)

    def check_password(self, password):
        """ Check if the password is correct or not.

        :param password: The password to check
        :type password: str
        :return: ``True`` or ``False`` depending of the password's validity
        :rtype: bool
        """
        return sha256_crypt.verify(password, self.password)

    def __repr__(self):
        return '<{}.{} (login: {}, level: {}, host: {}, nick: {})'.format(
            self.__class__.__module__,
            self.__class__.__qualname__,
            self.login, self.level, self.host, self.nick
        )

class UserList(dict):
    """ UserList is based on dict in order to have the username as the key and
    the user object as a value.

    The main goal here is to have ``__init__`` loading ``source`` and gather all
    the users from it.

    :param source: CSV file where are stored the users entries.
    :type source: str
    """
    def __init__(self, source):
        self._source = source

        with open(source, newline='') as file:
            for user in map(User, file.readlines()):
                self[user.login] = user

    def save(self):
        """ Save the data inside the csv file previously loaded by the
        ``__init__``.
        """
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
