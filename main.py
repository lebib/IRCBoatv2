#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from IRCBoat import IRCBoat
from IRCBoat.Plugins.Boat import BOAT_Boat
from config import BOAT

irc_boat = IRCBoat(
    BOAT['NICK'],
    BOAT['REALNAME'],
    BOAT['HOST'],
    BOAT['PORT'],
    BOAT['ENCODING'],
    BOAT['SSL']
)
boat = BOAT_Boat('Boat','Boat',irc_boat)
irc_boat.load_plugin(boat)
irc_boat.run_bot()
