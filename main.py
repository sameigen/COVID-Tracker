import requests
import sys
import covid
import commandline


def main():

    prompt = commandline.Prompt()
    prompt.prompt = '\033[1;31;40mCOVID-API> ' + '\033[0m'
    prompt.intro = '\033[94mCOVID console -> use command "help" for functions'
    prompt.cmdloop()

main()
