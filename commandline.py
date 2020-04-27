import sys
import cmd
import covid


class Prompt(cmd.Cmd):

    initial = covid.Covid()

    def do_stateResults(self, line):
        if(line):
            Prompt.initial.stateResults(line)
        else:
            print("Please type: stateResults (state Initials)")
            print("Ex: stateResults LA")

    def do_stateInfo(self, line):
        if(line):
            Prompt.initial.stateInfo(line)
        else:
            print("Please type: stateInfo (state Initials)")
            print("Ex: stateInfo NJ")


    def do_today(self, line):
        if(line):
            Prompt.initial.today(line)
        else:
            print("Please type: today (country Initials)")
            print("Ex: today USA")


    def do_exit(self, line):
        """exit - quit covid console"""
        sys.exit(1)
