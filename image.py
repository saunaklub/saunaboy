import os
import subprocess
import shlex
import random

def image(args):
    process = subprocess.Popen(['img2txt',
                                '-d', 'none',
                                '-W', '120',
                                '-f', 'irc',
                                args],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE)

    out, _ = process.communicate()

    return out.decode()
    

def pinup(args):
    directory = '/mnt/files/images/saunaboy/pinup/'
    filename = random.choice(os.listdir(directory))

    return image(directory+filename)
