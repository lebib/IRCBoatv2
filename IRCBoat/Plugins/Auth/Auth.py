from IRCBoat.Plugins.Auth import User


class Auth(object):
    """ Auth is the heart of the Auth plugin. It provide a certain amount
    of methods for manipulating easily the users.

    :param filename: CSV file where the data are stored.
    :type filename: string
    """
    def __init__(self, filename="USERS.csv"):
        self.filename = filename

    def add_user(self, login, password, level, nickname='', host=''):
        """ Create a new user in the database.

        :param login: User's login
        :param password: User's password
        :param level: User's level of rights
        :param nickname: User's current nickname
        :param host: User's current host
        :type login: str
        :type password: str
        :type level: int
        :type nickname: str
        :type host: str
        """
        user_list = User.UserList(self.filename)
        user_list[login] = User(
            ','.join([login,
                      User.hash_password(password),
                      str(level), nickname, host])
        )
        user_list.save()

    def delete_user(self, login):
        """ Delete the user assigned to the login given.

        :param login: User's login
        :type login: str
        """
        user_list = User.UserList(self.filename)
        del user_list[login]
        user_list.save()

    def update_user(self, login,
                    password=None, level=None, nickname=None, host=None):
        """ Modify an existent user.

        :param login: User's login
        :param password: User's password
        :param level: User's level of rights
        :param nickname: User's current nickname
        :param host: User's current host
        :type login: str
        :type password: str
        :type level: int
        :type nickname: str
        :type host: str
        """
        if self.is_user(login):
            user_list = User.UserList(self.filename)
            old_user = user_list[login]

            if password is not None:
                old_user.password = User.hash_password(password)
            if level is not None:
                old_user.level = level
            if nickname is not None:
                old_user.nickname = nickname
            if host is not None:
                old_user.host = host

            user_list[login] = User(
                "{},{},{},{},{}".format(
                    old_user.login,
                    old_user.password,
                    old_user.level,
                    old_user.nickname,
                    old_user.host
                )
            )
            user_list.save()

    def is_user(self, login):
        """ Return if the user assigned to the given login exists or not.

        :param login: User's login
        :type login: str
        :return: ``True`` if the user exists, ``False`` if not.
        :rtype: bool
        """
        user_list = User.UserList(self.filename)
        return login in user_list

    def is_user_connected(self, login):
        """ Return if the user assigned to the given login is connected or not.

        :param login: User's login
        :type login: str
        :return: ``True`` if the user is connected, ``False`` if not.
        :rtype: bool
        """
        if self.get_user(login):
            user_list = User.UserList(self.filename)
        return user_list[login].nickname != '' and user_list[login].host != ''

    def get_user(self, login):
        """ Return the user assigned to the given login.

        :param login: User's login
        :type login: str
        :return: ``User()`` if exists, ``None`` if not.
        :rtype: User / None
        """
        user_list = User.UserList(self.filename)
        if self.is_user(login):
            return user_list[login]
        else:
            return None
