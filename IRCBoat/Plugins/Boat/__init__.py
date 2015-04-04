import IRCBoat
from IRCBoat import Plugins.Plugin

class BOAT_Boat(plugin):
    def __init__(self, nick, realname):
        super().__init__("Boat",[])
        self.nick = nick
        self.realname = realname

    def on_connnect(self):
        """ Connecting to the server and join all the channels available.
        """
        IRCBoat.send('NICK', nick=self.nick)
        IRCBoat.send('USER', user=self.nick)
        #TODO: Do some functions for joining all the channels available.
        IRCBoat.send('JOIN', channel='#test')

    def on_disconnect(self):
        #TODO: Send a message for alerting that the bot he's disconnected.
        pass

    def on_ping(self, message):
        """ Answer to the server's ping.

        :param message: Message sent by the server
        :type message: str
        """
        IRCBoat.send('PONG', message=message)

    def on_user_join(self, nick, channel):
        """ Say hello to the newcomer.

        :param nick: Nick of the joining user
        :param channel: The channel joined
        :type nick: str
        :type channel: str
        """
        IRCBoat.send('PRIVMSG', target=nick, message="Salut " + nick)
        
    def join_all_channels(self):
        pass
