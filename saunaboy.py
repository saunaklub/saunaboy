import subprocess
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
    def on_connect(self):
         self.join(channel)

    def on_message(self, source, target, message):
        if(source == 'saunaboy'):
            if(not message.startswith(',')):
                self.message(message)

        print(source + ":" + target + "> " + message)
        self.greeting(source, target, message)

        if(message.startswith(',')):
            if(message == ',aufguss'):
                self.action(aufguss())
            if(message.startswith(',fortune')):
                self.message("")
                self.commandToChannel("fortune" + message[len(',fortune'):])
                self.message("")
            if(message == ',df'):
                self.commandToChannel("df -h | grep -v tmpfs | grep -v udev")
            if(message == ',health'):
                self.commandPreMessage(target)
                self.printRaidInfo()
                self.commandPostMessage(target)
            if(message == ',joke'):
                self.message(cyberjoke())
            if(message == ',meyers'):
                self.message(meyersItem())
            if(message == ',rezept'):
                self.message(rezeptChefkoch())
            if(message == ',cocktail'):
                self.action('macht eine Runde Cocktails:')
                self.message(cocktail())
            if(message.startswith(',image ')):
                self.message(image(message[len(',image '):]))
            if(message == ',pinup'):
                self.message(pinup())
            if(message.startswith(',action')):
                self.action(message[len(',action '):])
                
    def on_join(self, channel, user):
        if(user != 'saunaboy'):
            self.message(random.choice(welcome_messages).replace("<>", user))
                
    def commandPreMessage(self, user):
        self.message(random.choice(command_pre_messages).replace("<>", user))
        self.message(' ')

    def commandPostMessage(self, user):
        self.message(' ')
        self.message(random.choice(command_post_messages).replace("<>", user))

    def commandDenialMessage(self, user):
        self.message(random.choice(command_denial_messages).replace("<>", user))
        
    def printRaidInfo(self):
        self.message("Reporting RAID status: files.saunaklub.net")
        self.message(" ")

        self.commandToChannel("sudo mdadm --detail /dev/md0 | sed -n '13,+5p; 25,+4p'")

        message = ""
        for letter in ['b', 'c', 'd', 'e']:
            message += '/dev/sd' + letter + ': '
            message += self.commandToString('sudo smartctl -H /dev/sd' + letter +
                                            ' | grep "self-assessment test"')
        self.message(message)

    def commandToString(self, command):
        process = subprocess.Popen(['bash', '-c', command],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE)

        out, _ = process.communicate()
        return out.decode('utf-8')
        
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

    def action(self, action):
        self.message('\x01ACTION '+action+'\x01')
            
    def greeting(self, chan, nick, msg):
        greet_re = re.compile('hi', re.IGNORECASE)

        if greet_re.match(msg):
            reply = nick + ": " + random.choice(greet_messages)
            self.message(source, reply)

channel = '#saunaklub'
password = getpass.getpass("saunaboy password: ")
password = 'saunaboy:'+password

client = SaunaBoy('saunaboy', realname='Sven')
client.connect('chat.freenode.net', 6667,
               tls=False, tls_verify=False)
client.handle_forever()
