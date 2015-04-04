import bottom
from bottom import unpack
import asyncio

#TODO: Should be a Singleton class and the object/methods is shared between the
# plugins and commmands. The ideal is to list all the available on_functions
# inside the master plugin and then load them all when the plugin is loaded.
# The best way is w/o doubt to load only the functions derivate inside the
# plugin. There is no need to have useless functions inside the pile.
class IRCBoat(bottom.Client):
    """
    :param nick: IRC nickname
    :param realname: IRC realname
    :param host: Host of the IRC server
    :param port: Port of the IRC server
    :param encoding: Encoding used to get the IRC messages
    :param ssl: If using SSL or not
    :type nick: str
    :type realname: str
    :type host: str
    :type port: int
    :type encoding: str
    :type ssl: bool
    """
    def __init__(self, nick, realname, host, port, encoding='UTF-8', ssl=False):

        super().__init__(host, port, encoding, ssl)

        self.__add_event__('CLIENT_CONNECT', self.on_connect)
        self.__add_event__('CLIENT_DISCONNECT', self.on_disconnect)
        self.__add_event__('PING', self.on_ping)
        self.__add_event__('PRIVMSG', self.on_user_message)
        self.__add_event__('JOIN', self.on_user_join)

        self.nick, self.realname = nick, realname
        self.connection = Connection(host, port, self, encoding, ssl, True)

    def on_connect(self):
        """ Triggered when the bot is connecting.
        """
        self.send('NICK', nick=self.nick)
        self.send('USER', user=self.nick, realname = self.realname)
        #Will be replaced for joining all the channels.
        self.send('JOIN', channel='#test')

    def on_disconnect(self):
        """ Triggered when the bot is disconnecting
        """
        pass

    def on_ping(self, message):
        """ Triggered when the server start a ping.

        :param message: Ping's message
        :param type: str
        """
        self.send('PONG', message=message)

    def on_user_join(self):
        """ Triggered when an user is joining a channel where the bot is
        present.
        """
        pass

    def on_user_message(self, nick, target, message):
        """ Triggered when an user send a private message or a chan message.

        :param nick: Sender's IRC nick
        :param target: Sender's IRC target
        :param message: Sender's message
        :type nick: str
        :type target: str
        :type message: str
        """
        if nick == self.nick:
            pass # The bot wont answer to himself.
        if target == self.nick:
            pass # Private Message
        else:
            pass # Channel Message

    def run_bot(self):
        """ Handle the execution of the bot.
        """
        asyncio.get_event_loop().run_until_complete(super().run())

class Connection(bottom.connection.Connection):
    """ Connection is only a specialization of bottom.connection.Connection.
    The idea behind it it's to have access directly on the prompt all the
    messages from the server in order to easily debug the application.
    In the future it'll be print in a log file.

    :param host: Server's host
    :param port: Server's port
    :param encoding: Message's encoding
    :param ssl: SSL or not
    :param verbose: ``True`` Logs are printing in the shell
    :type host: str
    :type port: int
    :type encoding: str
    :type ssl: bool
    :type verbose: bool
    """
    def __init__(self, host, port, events, encoding, ssl, verbose):
        super().__init__(host, port, events, encoding, ssl)
        self.verbose = verbose

    @asyncio.coroutine
    def run(self, loop=None):
        yield from self.connect(loop=loop)
        while self.connected:
            msg = yield from self.read()
            if msg:
                try:
                    event, kwargs = unpack.unpack_command(msg)
                except ValueError:
                    print("PARSE ERROR {}".format(msg))
                else:
                    if self.verbose : print(msg)
                    yield from self.events.trigger(event, **kwargs)
