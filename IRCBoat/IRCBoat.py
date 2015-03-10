#!/usr/bin/python3.4
#-*- coding: utf-8 -*-

import bottom
import asyncio

class IRCBoat(bottom.Client):
    def __init__(self, nick, realname, host, port, encoding='UTF-8', ssl=False):
        super().__init__(host, port, encoding, ssl)
        self.nick, self.realname = nick, realname

    def connect(self):
        self.send('NICK', nick=self.nick)
        self.send('USER', user=self.nick, realname=self.realname)
        self.send('JOIN', channel='#test')

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

    def init_bot(self):
        self.__add_event__('CLIENT_CONNECT',self.connect)
        self.__add_event__('PRIVMSG', self.on_message)

irc_boat = IRCBoat('Boat', 'Boat is powerfull', 'irc.lebib.org', 6667)
irc_boat.init_bot()
asyncio.get_event_loop().run_until_complete(irc_boat.run())
