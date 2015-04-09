import bottom
from bottom import unpack
import asyncio


class IRCBoat(bottom.Client):
    def __init__(self, nick, realname, host, port, encoding='UTF-8', ssl=True):
        super().__init__(host, port, encoding, ssl)
        self.nick, self.realname = nick, realname
        self.host, self.port = host, port
        self.encoding, self.ssl = encoding, ssl
        self.connection = Connection(host, port, self, encoding, ssl, True)

    def run_bot(self):
        asyncio.get_event_loop().run_until_complete(super().run())

    def load_plugin(self, plugin):
        if self.validate_plugin(plugin):
            self.__add_event__('CLIENT_CONNECT', plugin.on_connect)
            self.__add_event__('CLIENT_DISCONNECT', plugin.on_disconnect)
            self.__add_event__('PING', plugin.on_ping)
            self.__add_event__('PRIVMSG', plugin.on_user_message)
            self.__add_event__('JOIN', plugin.on_user_join)

    def validate_plugin(self, plugin):
        return True


class Connection(bottom.connection.Connection):
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
                    if self.verbose:
                        print(msg)
                    yield from self.events.trigger(event, **kwargs)
