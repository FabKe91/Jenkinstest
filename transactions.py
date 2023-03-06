class TRX(object):
    OPTIONS = ["TEST", "x0815", "00"]

    def __init__(self):
        self._expression = ''

    def trigger(self, option):
        if option not in self.OPTIONS:
            raise TRXError("Invalid option '%s'." % option)
        self._expression += option
        if option == "x0815":
            raise TRXError("Transaction failed with option '%s'" % option)
        return self._expression

class TRXError(Exception):
    pass

