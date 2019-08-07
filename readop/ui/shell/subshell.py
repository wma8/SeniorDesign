from .shell import Shell


class SubShell(Shell):
    separator = Shell.separator

    def do_exit(self, user_input):
        return True

    def help_exit(self):
        print('Returns to the ReadOp main shell.')
