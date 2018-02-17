#!/usr/bin/python3
'''
The file that sets up the console class to be used to access data for HBnB
'''
import cmd
import models
import shlex


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
        print()
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
        if not argument:
            print("** class name missing **")
        elif argument not in models.available_models:
            print("** class doesn't exist **")
        else:
            instance_create = models.available_models[argument]()
            print(instance_create.id)
            models.storage.save()

    def do_show(self, argument):
        '''
        Prints the string representation of an instance based on class and id
        '''
        arguments = shlex.split(argument)
        if len(arguments) == 0:
            print("** class name missing **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif arguments[0] not in  models.available_models:
            print("** class doesn't exist **")
        else:
            stored_key = "{}.{}".format(arguments[0], arguments[1])
            file_stored = models.storage.all()
            if stored_key in file_stored:
                print(file_stored[stored_key])
            else:
                print("** no instance found **")

    def do_destroy(self, argument):
        '''
        Destroys an instance based on class and id
        '''
        arguments = shlex.split(argument)
        if len(arguments) == 0:
            print("** class name missing **")
            return
        elif len(arguments) == 1:
            print("** instance id missing **")
            return
        try:
            instance_name = arguments[0]
            instance_id = arguments[1]
            eval(instance_name)
        except NameError:
            print("** class doesn't exist **")
            return
        file_stored = models.storage.all()
        for i in file_stored.values():
            if instance_name == i.__class__.__name__ and instance_id == i.id:
                del i
                models.storage.save()
                return
        print("** no instance found **")
        models.storage.save()

    def do_all(self, argument):
        '''
        Prints all the instances based on class.
        If no class specified all instances print.
        '''
        arguments = shlex.split(argument)
        instance_list = []
        instance_dictionary = models.storage.all()
        if len(arguments) == 0:
            for key, value in instance_dictionary.items():
                instance_list.append(value)
            print(instance_list)
        elif arguments[0] not in models.available_models:
            print("** class doesn't exist **")
        else:
            for key, value in instance_dictionary.items():
                if arguments[0] in key:
                    instance_list.append(value)
            print(instance_list)

    def do_update(self, argument):
        '''
        Updates an instance based on class and id by adding or updating
        the attribute. (saves changes to JSON file)
        '''
        arguments = shlex.split(argument)
        if len(arguments) == 0:
            print("** class name missing **")
            return
        elif len(arguments) == 1:
            print("** instance id missing **")
            return
        elif len(arguments) == 2:
            print("** attribute name missing **")
            return
        elif len(arguments) == 3:
            print("** value missing **")
            return
        try:
            eval(arguments[0])
        except NameError:
            print("** class doesn't exist **")
            return
        instance_key = arguments[0] + "." + arguments[1]
        instance_dictionary = models.storage.all()
        try:
            instance_value = instance_dictionary[instance_key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attribute_type = type(getattr(instance_value, arguments[2]))
            arguments[3] = attribute_type(arguments[3])
        except AttributeError:
            pass
        setattr(instance_value, arguments[2], arguments[3])
        models.storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
