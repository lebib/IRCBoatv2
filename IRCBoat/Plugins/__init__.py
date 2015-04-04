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

    def __init__(self, name, commands=[]):
        #TODO: bot_name will be changed and updated when IRCBoat will load the
        #plugin.
        self.name = name
        self.bot_name = ''
        self.commands = commands

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
        if nick == self.bot_name:
            pass
        else:
            handle_command(nick, message)

    def on_user_join(self):
        """ Triggered
        pass

    def handle_command(self, nick, message):
        """ Manage the use of the command.
        """

        :param nick: Sender's IRC nick
        :param message: Sender's IRC message
        :type nick: str
        :type message: str
        """
        message = self.process_command(message)
        if self.name == message[0]:
            for command in self.commands:
                if command.name == message[1]:
                    command.trigger(message[2:])
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

class Command(object):
    """ Command is the master class for the commands. As the Plugin's class do,
    Command provide some functionality to create your own commands for your
    plugins.

    :param name: Command's name
    :param level: Right's level required for using it
    :type name: str
    :type level: int
    """

    def __init__(self, name, level=0):
        self.name = name
        self.level = level

    def trigger(self, args):
        """ Trigger the content when the command is called.

        :param args: Arguments list
        :type args: list[str(),...]
        """
        pass
