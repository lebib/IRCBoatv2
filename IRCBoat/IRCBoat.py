 #!/usr/bin/python3.4
#-*- coding: utf-8 -*-

import bottom
from bottom import unpack
import asyncio

class IRCBoat(bottom.Client):
    def __init__(self, nick, realname, host, port, encoding='UTF-8', ssl=False):
        super().__init__(host, port, encoding, ssl)
        self.__add_event__('CLIENT_CONNECT',self.connect)
        self.__add_event__('PRIVMSG', self.on_message)
        self.__add_event__('PING', self.pong)
        self.nick, self.realname = nick, realname
        self.connection = BOATConnection(host, port, self, encoding, ssl, True)

    def connect(self):
        self.send('NICK', nick=self.nick)
        self.send('USER', user=self.nick, realname=self.realname)
        self.send('JOIN', channel='#test')

    def pong(self, message):
        self.send('PONG', message=message)

    def on_message(self, nick, target, message):
        if nick == self.nick:
            pass
        if target == self.nick:
            msg = "I'm too dumb to answer you correctly."
            self.send('PRIVMSG', target=nick, message=msg)
        else:
            if message[0] == '!':
                msg = "This command is not available."
                self.send('PRIVMSG', target=target, message=msg)

    def run(self):
        asyncio.get_event_loop().run_until_complete(super().run())

class BOATConnection(bottom.connection.Connection):
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
                    print(msg)
                    yield from self.events.trigger(event, **kwargs)

irc_boat = IRCBoat('Boat', 'Boat is powerfull', 'irc.lebib.org', 6667)
irc_boat.run()
