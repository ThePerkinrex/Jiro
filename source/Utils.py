import re
import Tokens


var_id = '^[A-Za-z_]\w*$'
var_id_mid = '[A-Za-z_]\w*'

class LogColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    RESPONSE = '\033[1;36m'
    LANG = '\033[1;34m'
    WARNING = '\033[93m'  # WARNINGS
    FAIL = '\033[91m'  # ERRORS & END
    SETUP = '\033[32m'  # SETUP
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def psinit():
    print(LogColors.SETUP + "\n\n ################### - WELCOME TO - ###################")
    print(" #                                                    #")
    print(" #   ____               ____            _       _     #")
    print(" #  |  _ \ ___ _ __ ___/ ___|  ___ _ __(_)_ __ | |_   #")
    print(" #  | |_) / _ \ '__/ __\___ \ / __| '__| | '_ \| __|  #")
    print(" #  |  __/  __/ | | (__ ___) | (__| |  | | |_) | |_   #")
    print(" #  |_|   \___|_|  \___|____/ \___|_|  |_| .__/ \__|  #")
    print(" #                                       |_|          #")
    print(" #                                                    #")
    print(" ######################################################\n\n" + LogColors.ENDC)

def listtostring(mylist):
    r = "["
    for item in mylist:
        r = r + item + ","
    r = r.rstrip(",") + "]"
    return r


def ps_help(invokeName):
    print("------------| PercScript Help |------------")
    print(invokeName + " <filepath> -> run the PercScript file in <filepath>")
    print(invokeName + " -> print this help message")
    print(invokeName + " -h -> print this help message")
    print("\n\n")


def error(name, text, line):
    print(LogColors.FAIL + "\n----------- ERROR -----------\n" + name)
    print("in " + text)
    print("line " + str(line) + LogColors.ENDC)
    quit(1)

def log(verbose, *text):
    if verbose:
        r = ''
        for t in text:
            r += str(t) + ' '
        print(r)


def call_native(name, args):
    # print("Native func " + name + " getting called with args " + str(args))
    if name == 'print':
        print(args[0])


def replace_regex(base: str, regex: str, replacing: str):
    m = re.search(regex, base)
    if m:
        return base.replace(m.group(0), replacing)
    return None


def val_to_ps(val):
    if type(val) == str:
        return str('"' + val + '"')
    elif type(val) == int:
        return str(val)


def tokenize(s: str, text, line, parser=None):
    t = None
    if parser:
        m = re.search(var_id_mid, s)
        if m:
            s = s.replace(m.group(0), '"' + m.group(0) + '"')
    for token in Tokens.valid_token_literals:
        m = re.search('^' + token[0] + '$', s)

        if m:
            t = token[1](m.groups(), text, line)
            break
    if t is None:
        error(str(s) + ' is not a valid token', text, line)
    return t
