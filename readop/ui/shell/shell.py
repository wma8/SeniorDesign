import cmd


class Shell(cmd.Cmd):
    separator = '=' * 100 + '\n'

    instruction_for_help = 'Type \'help\' or \'?\' to list commands.\n'

    def do_exit(self, user_input):
        print('Goodbye.')
        return True

    def help_exit(self):
        print('Exits the shell.')
