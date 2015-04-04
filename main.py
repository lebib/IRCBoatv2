#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from IRCBoat import IRCBoat
from config import BOAT
irc_boat = IRCBoat.IRCBoat(
    BOAT['NICK'],
    BOAT['REALNAME'],
    BOAT['HOST'],
    BOAT['PORT'],
    BOAT['ENCODING'],
    BOAT['SSL']
)
irc_boat.run_bot()
