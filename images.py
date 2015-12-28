import os
import subprocess
import shlex
import random

def pinup():
    directory = '/mnt/raid/images/saunaboy/pinup/'
    image = random.choice(os.listdir(directory))

    process = subprocess.Popen(['img2txt',
                                '-d', 'none',
                                '-W', '120',
                                '-f', 'irc',
                                directory+image],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE)

    out, _ = process.communicate()

    return out.decode()
