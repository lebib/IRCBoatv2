#!/usr/bin/python3.4
#-*- coding: utf-8 -*-

import bottom
import asyncio
from IRCBoat import IRCBoat

boat = IRCBoat('Boat', 'Small boat powerfull', 'irc.lebib.org', 6667)
boat.init_boat()
asyncio.get_event_loop().run_until_complete(irc_boat.run())
