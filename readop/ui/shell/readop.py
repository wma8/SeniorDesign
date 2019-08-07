from .analytics import AnalyticsShell
from .database import DatabaseShell
from .parameters import ParameterShell
from .shell import Shell


class ReadopShell(Shell):
    intro = \
        Shell.separator +\
        'Welcome to ReadOp.\n' + \
        Shell.instruction_for_help + \
        Shell.separator

    prompt = 'readop > '

    def __init__(self):
        super().__init__()
        self.database_shell = DatabaseShell()
        self.parameter_shell = ParameterShell()
        self.analytics_shell = AnalyticsShell()

    def do_database(self, user_input):
        self.database_shell.cmdloop()
        print(self.intro)

    def help_database(self):
        print('Enters the ReadOp database subsystem.')

    def do_parameters(self, user_input):
        self.parameter_shell.cmdloop()
        print(self.intro)

    def help_parameters(self):
        print('Enters the ReadOp parameter subsystem.')

    def do_analytics(self, user_input):
        self.analytics_shell.cmdloop()
        print(self.intro)

    def help_analytics(self):
        print('Enters the ReadOp analytics subsystem.')
