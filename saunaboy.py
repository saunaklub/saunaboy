import shlex
import random
import time
import pydle
import getpass

from aufguss import *
from joke import *
from meyers import *
from rezept import *
from cocktail import *
from image import *
from commands import *

dnd_messages = [
    "please do not disturb our conversation.",
    "we are having a conversation here."]

welcome_messages = [
    "<>! It's an honor.",
    "Hey <>, what's crackin'?",
    "Hi <>, how ye doin'?",
    "Salut <>!",
    "Bonjour <>.",
    "Moin <>.",
    "Tach <>!"
]

command_pre_messages = [
    "But of course, master <>!",
    "Your wish is my command, <>.",
    "Aye aye, Sir!",
    "For you <>? Anytime!",
    "It's an honor to serve you, <>."
]

command_post_messages = [
    "Is that all for now?",
    "Anything else you desire <>?",
    "If you need anything else, I'm here for you."
]

command_denial_messages = [
    "You did not seriously expect that to work, <>...",
    "Yeah, right.",
    "Nice try <>.",
    "Forget it.",
    "Better luck next time <>!",
    "Sorry <>, but I take orders only from my creator.",
    "Fuck off.",
    "Leave me alone."
]

class SaunaBoy(pydle.MinimalClient):

    def __init__(self, nick, realname):
        super().__init__(nick, realname=realname)
        self.nick = nick

        self.message_map = {
            'raid' : (raidInfo, "Gebe files.saunaklub.net RAID Statusinformation aus."),
            'fortune' : (fortune, "Generiere 'fortune' mit optionalen Argumenten."),
            'witz' : (cyberjoke, "Reiße einen von Großmeister Al Lowe's Witzen."),
            'meyers' : (meyersItem, "Gebe zufälliges Kapitel aus Scott Meyers' \"Effective C++\" Serie aus."),
            'rezept' : (rezeptChefkoch, "Gebe das Rezept des Tages von chefkoch.de aus."),
            'cocktail' : (cocktail, "Gebe einen zufälliges Mixgetränk von cocktaildb.com aus."),
            'bild ' : (image, "Zeige ein Bild mit libcaca's img2txt an."),
            'pinup' : (pinup, "Zeige ein zufälliges Pin-Up Bild an."),
            'aktion' : (action, "Führe das Argument als Aktion aus."),
            'hilfe' : (self.usage, "Gebe alle verfügbaren Kommandos aus."),
        }

        self.action_map = {
            'aufguss' : (aufguss, "Mache einen Sauna-Aufguss, grosse Auswahl an Aromen!"),
        }

        self.command_map = {
            'df' : ("df -h | grep -v tmpfs | grep -v udev", "Zeige Festplatten-Auslastung mit df an."),
        }

        self.function_map = {
            'nick' : (self.set_nickname, "Setze den IRC-Spitznamen.")
        }

    def usage(self, args):
        width = 10
        message = "Nutzbare Kommandos, mit ',' als Präfix:\n\n"
        for k, v in SaunaBoy.message_map.items():
            message += k.ljust(10) + v[1] + '\n'
        for k, v in SaunaBoy.action_map.items():
            message += k.ljust(10) + v[1] + '\n'
        for k, v in SaunaBoy.command_map.items():
            message += k.ljust(10) + v[1] + '\n'
        for k, v in SaunaBoy.function_map.items():
            message += k.ljust(10) + v[1] + '\n'
        return message

    def set_nickname(self, nick):
        self.nick = nick
        super().set_nickname(nick)

    def on_connect(self):
         self.join(channel)

    def on_message(self, source, target, message):
        if(source == self.nick):
            if(not message.startswith(',')):
                self.message(message)

        print(source + ":" + target + "> " + message)
        self.greeting(source, target, message)

        if(message.startswith(',')):
            command = ""
            args = ""
            if(message.find(" ") != -1):
                command = message[1:message.find(" ")]
                args = message[message.find(" ")+1:]
            else:
                command = message[1:]

            if(command in self.message_map):
                print(self.message_map[command][0])
                self.message(self.message_map[command][0](args))
            if(command in self.action_map):
                print("action: " + command)
                self.message(action(self.action_map[command][0](args)))
            if(command in self.command_map):
                commandToChannel(self.command_map[command][0])
            if(command in self.function_map):
                print(args)
                self.function_map[command][0](args)

    def on_join(self, channel, user):
        if(user != self.nick):
            self.message(random.choice(welcome_messages).replace("<>", user))

    def commandPreMessage(self, user):
        self.message(random.choice(command_pre_messages).replace("<>", user))
        self.message(' ')

    def commandPostMessage(self, user):
        self.message(' ')
        self.message(random.choice(command_post_messages).replace("<>", user))

    def commandDenialMessage(self, user):
        self.message(random.choice(command_denial_messages).replace("<>", user))

    def commandToChannel(self, command):
        process = subprocess.Popen(['bash', '-c', command],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)
        out, _ = process.communicate()
        out = out.decode('utf-8').rstrip('\n').replace('\r', '').expandtabs(tabsize=8)
        self.message(out)

    def message(self, message):
            print(message)
            super().message(channel, message)

    def greeting(self, chan, nick, msg):
        greet_re = re.compile('hi', re.IGNORECASE)

        if greet_re.match(msg):
            reply = nick + ": " + random.choice(greet_messages)
            self.message(source, reply)

channel = '#saunaklub'
password = getpass.getpass("saunaboy password: ")
password = 'saunaboy:'+password

client = SaunaBoy(nick='saunaboy', realname='Sven')
client.connect('chat.freenode.net', 6667,
               tls=False, tls_verify=False)
client.handle_forever()
