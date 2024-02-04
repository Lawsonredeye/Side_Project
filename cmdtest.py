#!/usr/bin/env python3

"""This Modules is just for practicing how to use the cmd module
like writing our own command interpreter and more
"""
import cmd

class Interpreter(cmd.Cmd):
    """
    using a class to inherits from the cmd.Cmd module to have access to its properties and methods

    Args:
        cmd.Cmd: a class being passes as a parameter
        to the interpreter class.
    """
    def do_greet(self, person):
        """
        Greets the incoming Dev as a sign of peace ^__^
        """
        print(f"welcome, {person}")

    def do_EOF(self, line):
        """
        Terminates the program and tells user its logging off
        """
        print("Logging Off!")
        return True
    
    # def create(self, person):
    #     self.name = person

if __name__ == "__main__":
    Interpreter().cmdloop()
