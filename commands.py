class commands:
    def __init__(self, args):
        self.args = args
        self.clist = "-h, --help, --options, -o, -examples -e, --date "

    def is_command(self, arg):

        if type(arg) is str and  arg in self.clist:
            pass
            

