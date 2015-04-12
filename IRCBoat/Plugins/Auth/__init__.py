from IRCBoat.Plugins import Plugin, Command
from Auth import Auth


class BOAT_Auth(Plugin):
    def __init__(self):
        super().__init__("Auth", [
                         Command("register", 0, self.register),
                         Command("login", 0, self.login),
                         Command("disconnect", 0, self.disconnect)
                         ])
        self.auth = Auth('USERS.csv')

    def register(self, nick, host, args):
        if len(args) != 3:
            return  # invalid number of arguments
        if self.auth.is_user(args[0]):
            return  # user already exists
        self.auth.add_user(args[0], args[1], 1, nick, host)

    def login(self, nick, host, args):
        if len(args) != 2:
            return  # invalid number of arguments
        user = self.auth.get_user(args[0])
        if user is None:
            return  # user does not exist
        if not user.check_password(args[1]):
            return  # password is not valid
        self.auth.update_user(args[0], nickname=nick, host=host)

    def disconnect(self, nick, host, args):
        if len(args) != 0:
            return
        if self.auth.user_is_connected(args[0]):
            self.auth.update_user(args[0], nickname="", host="")
