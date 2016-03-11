import subprocess

def translate(args):
    argv = args.split(' ')
    process = subprocess.Popen(['trans',
                                argv[0], " ".join(argv[1:])],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)

    out, _ = process.communicate()

    return out.decode()
