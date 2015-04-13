from IRCBoat.Plugins import Plugin, Command
from IRCBoat.Plugins.Auth.Auth import Auth


class BOAT_Auth(Plugin):
    def __init__(self, irc_boat):
        super().__init__("Auth", irc_boat, [
                         Command("register", 0, self.register),
                         Command("login", 0, self.login),
                         Command("disconnect", 0, self.disconnect)
                         ])
        self.auth = Auth('USERS.csv')

    def register(self, nick, host, args):
        if len(args) != 2:
            print(len(args))
            self.send_error_message("register", nick,
                                    "Invalid number of arguments.")
            return
        if self.auth.is_user(args[0]):
            self.send_error_message("register", nick,
                                    "User already exists.")
            return
        self.auth.add_user(args[0], args[1], 1, nick, host)

    def login(self, nick, host, args):
        if len(args) != 2:
            self.send_error_message("login", nick,
                                    "Invalid number of arguments.")
            return
        user = self.auth.get_user(args[0])
        if user is None:
            self.send_error_message("login", nick,
                                    "User does not exists.")
            return
        if not user.check_password(args[1]):
            self.send_error_message("login", nick,
                                    "Password is not valid.")
            return
        self.auth.update_user(args[0], nickname=nick, host=host)

    def disconnect(self, nick, host, args):
        if len(args) != 0:
            self.send_error_message("disconnect", nick,
                                    "Invalid number of arguments.")
            return
        if self.auth.is_user_connected(args[0]):
            self.auth.update_user(args[0], nickname="", host="")
        else:
            self.send_error_message("disconnect", nick,
                                    "You're not connected.")
