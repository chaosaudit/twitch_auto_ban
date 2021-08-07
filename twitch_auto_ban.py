import socket
import time
import os.path

#  Details of the account doing the banning. Auth token can be generated here: https://twitchapps.com/tmi/

NICK = "moderator_name"
auth_token = "oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#  The channel to ban from (keep the # at the beginning of the channel name)

CHAN = "#twitch_channel"

#  Add a reason for banning or leave blank ("") if not needed

ban_message = "spam bot"


####################################################
### - No need to modify anything below this line ###
####################################################

#  Twitch IRC chat server details
HOST = "irc.twitch.tv"
PORT = 6667

#  Check if banlist.txt exists
if not os.path.isfile("banlist.txt"):
	quit("banlist.txt not found")

#  Connect to IRC and send user/auth info
con = socket.socket()
con.connect((HOST, PORT))
con.send(str.encode("USER " + HOST + "\r\n"))
con.send(str.encode("PASS " + auth_token + "\r\n"))
con.send(str.encode("NICK " + NICK.lower() + "\r\n"))
con.send(str.encode("JOIN " + CHAN.lower() + "\r\n"))

#  Send IRC message with a ban command for each username in the input file
with open("banlist.txt", "r") as infile:

    for name in infile.readlines():

        print(f"Banning {name.strip()}")
        con.send(str.encode(f"PRIVMSG {CHAN.lower()} :/ban {name.strip()} {ban_message}\r\n"))
        time.sleep(0.1)

con.close()

