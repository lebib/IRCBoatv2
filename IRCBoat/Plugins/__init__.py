class Plugin(object):

    def __init__(self, name, bot_name):
        self.name = name
        self.commands = []
        self.bot_name = bot_name

    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_user_message(self, nick, target, message):
        if nick == self.bot_name:
            pass
        else:
            handle_command(nick, message)

    def on_user_join(self):
        pass

    def handle_command(self, nick, message):
        message = self.process_command(message)
        if self.name == message[0]:
            for command in self.commands:
                if command.name == message[1]:
                    command.trigger(message[2:])
                    pass

    def process_command(self, message):
        if message[0] == '!':
            message = message[1:]
        return message.split(' ')

class Command(object):

    def __init__(self, name, level=0):
        self.name = name
        self.level = level

    def trigger(self, args):
        pass
