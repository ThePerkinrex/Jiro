#!/usr/bin/env python3

#   ____               ____            _       _
#  |  _ \ ___ _ __ ___/ ___|  ___ _ __(_)_ __ | |_
#  | |_) / _ \ '__/ __\___ \ / __| '__| | '_ \| __|
#  |  __/  __/ | | (__ ___) | (__| |  | | |_) | |_
#  |_|   \___|_|  \___|____/ \___|_|  |_| .__/ \__|
#                                       |_|

import sys

import PSParser
import Utils

print(Utils.LogColors.SETUP + "\n\n ################### - WELCOME TO - ###################")
print(" #                                                    #")
print(" #   ____               ____            _       _     #")
print(" #  |  _ \ ___ _ __ ___/ ___|  ___ _ __(_)_ __ | |_   #")
print(" #  | |_) / _ \ '__/ __\___ \ / __| '__| | '_ \| __|  #")
print(" #  |  __/  __/ | | (__ ___) | (__| |  | | |_) | |_   #")
print(" #  |_|   \___|_|  \___|____/ \___|_|  |_| .__/ \__|  #")
print(" #                                       |_|          #")
print(" #                                                    #")
print(" ######################################################\n\n" + Utils.LogColors.ENDC)

args = sys.argv
invokeName = args.pop(0)

# print("Passed arguments: " + Utils.listtostring(args))

if args.__len__() == 0:
    Utils.ps_help(invokeName)
else:
    if args[0] == '-h':
        Utils.ps_help(invokeName)
    else:
        p = PSParser.Parser()
        p.parse(open(args[0]).readlines(), True)
