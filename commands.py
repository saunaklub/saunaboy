import subprocess

def action(args):
    return '\x01ACTION '+args+'\x01'

def commandToString(command):
    process = subprocess.Popen(['bash', '-c', command],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE)

    out, _ = process.communicate()
    return out.decode('utf-8').replace("\t", "        ")

def sanitizeArgs(args):
    if(";" in args or
       "\\" in args or
       "`" in args or
       "$" in args or
       "|" in args or
       ">" in args or
       "<" in args):
        return ""

    return args


def raidInfo(args):
    message = "Reporting RAID status: files.saunaklub.net\n\n"
    message += commandToString("sudo mdadm --detail /dev/md0 | sed -n '13,+5p; 25,+4p'")

    message += "\n"
    for letter in ['b', 'c', 'd', 'e']:
        message += '/dev/sd' + letter + ': '
        message += commandToString('sudo smartctl -H /dev/sd' + letter +
                                          ' | grep "self-assessment test"')
        message += '\n'
        
    return message


def fortune(args):
    message = "\n"
    message += commandToString("fortune " + args)
    return message
