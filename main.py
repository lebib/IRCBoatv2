#!/usr/bin/python3.4
#-*- coding: utf-8 -*-

import bottom
import asyncio

NICK = 'Boat'
CHANNEL = '#test'

boat = bottom.Client('irc.lebib.org', 6667, ssl=False)

@boat.on('CLIENT_CONNECT')
def connect():
    boat.send('NICK', nick=NICK)
    boat.send('USER', user=NICK, realname='Small boat powerfull')
    boat.send('JOIN', channel=CHANNEL)

@boat.on('PING')
def pong(message):
    boat.send('PONG', message=message)

@boat.on('PRIVMSG')
def message(nick, target, message):
    if nick == NICK:
        return
    if target == NICK:
        msg = "I'm too dumb to answer you correctly."
        boat.send('PRIVMSG', target=nick, message=msg)
    else:
        if message[0] == '!':
            msg = "This command is not available."
            boat.send('PRIVMSG', target=target, message=msg)

asyncio.get_event_loop().run_until_complete(bot.run())
