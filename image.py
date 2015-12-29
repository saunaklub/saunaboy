import os
import subprocess
import shlex
import random

def image(path):
    process = subprocess.Popen(['img2txt',
                                '-d', 'none',
                                '-W', '120',
                                '-f', 'irc',
                                path],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE)

    out, _ = process.communicate()

    return out.decode()
    

def pinup():
    directory = '/mnt/raid/images/saunaboy/pinup/'
    image = random.choice(os.listdir(directory))

    return image(directory+image)
