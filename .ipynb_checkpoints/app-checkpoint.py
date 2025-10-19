from webbot import *
import pyautogui
import argparse
import sys
import time


def getOptions(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(description="This bot helps users to mass report accounts with clickbaits or objectionable material.")
    parser.add_argument("-u", "--username", type = str, default = "", help = "Username to report.")
    parser.add_argument("-f", "--file", type = str, default = "acc.txt", help = "Accounts list ( Defaults to acc.txt in program directory ).")

    options = parser.parse_args(args)

    return options


ans=getOptions()

