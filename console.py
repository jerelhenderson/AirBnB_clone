#!/usr/bin/python3
'''
The file that sets up the console class to be used to access data for HBnB
'''


import cmd


class HBNBCommand(cmd.Cmd):
    '''
    The class methods to setup the console
    '''
    prompt = '(hbnb) '

    def do_quit(self, arguments):
        '''
        Defines the quit function
        '''
        return True

    def do_EOF(self, arguments):
        '''
        Defines the action to take when the console receives EOF signal
        '''
        return True
    
    def emptyline(self):
        '''
        Makes inputting an emptyline in the console do nothing
        '''
        pass
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
