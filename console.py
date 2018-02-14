#!/usr/bin/python3
'''
The file that sets up the console class to be used to access data for HBnB
'''
import cmd
import json
import shlex
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    '''
    The class methods to setup the console
    '''
    prompt = '(hbnb) '

    def do_quit(self, argument):
        '''
        Defines the quit function
        '''
        return True

    def do_EOF(self, argument):
        '''
        Defines the action to take when the console receives EOF signal
        '''
        return True

    def emptyline(self):
        '''
        Makes inputting an emptyline in the console do nothing
        '''
        pass

    def do_create(self, argument):
        '''
        Creates an instance of BaseModel
        '''
        if argument == "":
            print("** class name missing **")
        elif models.available_models.get(argument) is None:
            print("** class doesn't exist **")
        else:
            created = models.available_models[argument]()
            created.save()
            print(created.id)

    def do_show(self, argument):
        '''
        Prints the string representation of an instance based on class and id
        '''
if __name__ == "__main__":
    HBNBCommand().cmdloop()
