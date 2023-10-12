#!/usr/bin/python3
import cmd
class my_console_cmd(cmd.Cmd):
    prompt = ">>>>"

    def emptyline(self):
        """
        This method handles empty lines.
        """
        pass

    def do_quit(self, line):
        """ 
        Quit the console.
        """
        return True

    def do_EOF(self, line):
        """
        Exit the console.
        """
        return True 

if __name__ == '__main__':
    my_console = my_console_cmd()
    my_console.cmdloop()
