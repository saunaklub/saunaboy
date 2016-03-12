import subprocess

def wiki(args):
    process = subprocess.Popen(['wiki', args],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)

    out, _ = process.communicate()

    return out.decode()
    
