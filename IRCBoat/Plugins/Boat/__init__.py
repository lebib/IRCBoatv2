import IRCBoat
from IRCBoat.Plugins import Plugin

class BOAT_Boat(Plugin):
    def __init__(self, nick, realname, irc_boat):
        super().__init__("Boat",[])
        self.nick = nick
        self.realname = realname
        self.irc_boat = irc_boat

    def on_connnect(self):
        """ Connecting to the server and join all the channels available.
        """
        self.irc_boat.send('NICK', nick=self.nick)
        self.irc_boat.send('USER', user=self.nick)
        #TODO: Do some functions for joining all the channels available.
        self.irc_boat.send('JOIN', channel='#test')

    def on_disconnect(self):
        #TODO: Send a message for alerting that the bot he's disconnected.
        pass

    def on_ping(self, message):
        """ Answer to the server's ping.

        :param message: Message sent by the server
        :type message: str
        """
        self.irc_boat.send('PONG', message=message)

    def on_user_join(self, nick, channel):
        """ Say hello to the newcomer.

        :param nick: Nick of the joining user
        :param channel: The channel joined
        :type nick: str
        :type channel: str
        """
        self.irc_boat.send('PRIVMSG', target=channel, message="Salut " + nick)

    def on_user_message(self, nick, target, message):
        super().on_user_message(nick, target, message)
        
    def join_all_channels(self):
        pass