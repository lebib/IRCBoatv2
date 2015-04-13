class Plugin(object):
    """ Plugin is the master class for making plugins.
    You need to derivate from it in order to make
    proper plugins. It provides all the basic features and
    acces you need.

    :param name: Plugin's name.
    :param bot_name: Current Bot's name.
    :param commands: Plugin's commands.
    :type name: str
    :type bot_name: str
    :type commands: list[Command(),...]
    """

    def __init__(self, name, irc_boat, commands=[]):
        self.name = name
        self.irc_boat = irc_boat
        self.commands = commands

    def on_ping(self):
        pass

    def on_connect(self):
        """ Triggered when the bot is connecting.
        """
        pass

    def on_disconnect(self):
        """ Triggered when the bot is disconnecting.
        """
        pass

    def on_user_message(self, nick, target, message):
        """ Triggered when the bot listen a message.

        :param nick: Sender's IRC nick
        :param target: Sender's target
        :param message: Sender's message
        :type nick: str
        :type target: str
        :type message: str
        """
        if nick == self.irc_boat.nick:
            pass
        else:
            self.handle_command(nick, message)

    def on_user_join(self, nick, channel):
        """ Triggered when an user is joining a channel where the bot is
        present.

        :param nick: Nick of the joining user
        :param channel: The channel joined
        :type nick: str
        :type channel: str
        """
        pass

    def handle_command(self, nick, message):
        """ Manage the use of the command.

        :param nick: Sender's IRC nick
        :param message: Sender's IRC message
        :type nick: str
        :type message: str
        """
        message = self.process_command(message)
        if self.name == message[0]:
            print("searching command")
            for command in self.commands:
                if command.name == message[1]:
                    print("command found")
                    print(message)
                    print(message[2:])
                    command.trigger(nick=nick, host="", args=message[2:])
                    pass

    def process_command(self, message):
        """ Remove the bang of the message and split between
        the arguments.

        :param message: Message to process
        :type message: str
        :return: List of the message arguments.
        :rtype: list[str(),...]
        """
        if message[0] == '!':
            message = message[1:]
        return message.split(' ')

    def send_error_message(self, command, nick, message):
        # msg = "ERROR {}.{} {}".format(self.name, command, message)
        print(message)
        # self.irc_boat.send('PRIVMSG', target=nick, message=message)


class Command(object):
    """ Command is the master class for the commands. As the Plugin's class do,
    Command provide some functionality to create your own commands for your
    plugins.

    :param name: Command's name
    :param level: Right's level required for using it
    :param function: Function triggered when user is calling the command.
    :type name: str
    :type level: int
    :type function: function
    """

    def __init__(self, name, level, function):
        self.name = name
        self.level = level
        self.function = function

    def trigger(self, nick="", host="", args=[]):
        """ Trigger the content when the command is called.

        :param args: Arguments list
        :type args: list[str(),...]
        """
        self.function(nick, host, args)
