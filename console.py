#!/usr/bin/env python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        print("")
        return True
    
    def help_quit(self):
        print("Quit command to exit the program\n")
    
    do_EOF = do_quit

if  __name__ == "__main__":
    HBNBCommand().cmdloop()
