import re


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


def tokenize(s):
    pass
