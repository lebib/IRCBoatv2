#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import IRCBoat
from IRCBoat.Plugins.Boat import BOAT_Boat
from IRCBoat.Plugins.Auth import BOAT_Auth
from config import BOAT

irc_boat = IRCBoat.IRCBoat(
    BOAT['NICK'],
    BOAT['REALNAME'],
    BOAT['HOST'],
    BOAT['PORT'],
    BOAT['ENCODING'],
    BOAT['SSL']
)
boat = BOAT_Boat(irc_boat)
irc_boat.load_plugin(boat)
auth = BOAT_Auth(irc_boat)
irc_boat.load_plugin(auth)
irc_boat.run_bot()
