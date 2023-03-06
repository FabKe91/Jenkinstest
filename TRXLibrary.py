from transactions import TRX, TRXError


class TRXLibrary(object):
    """Test library for testing *TRX* business logic.

    Interacts with PDiag  directly using ????
    """

    def __init__(self):
        self._trx = TRX()
        self._result = ''

    def trigger_transaction(self, option):
        """ """
        self._result = self._trx.trigger(option)

    def result_should_be(self, expected):
        """Verifies that the current result is ``expected``.

        """
        if self._result != expected:
            raise AssertionError('%s != %s' % (self._result, expected))

    def should_cause_error(self, expression):
        """Verifies that calculating the given ``expression`` causes an error.

        The error message is returned and can be verified using, for example,
        `Should Be Equal` or other keywords in `BuiltIn` library.

        Examples:
        | Should Cause Error | invalid            |                   |
        | ${error} =         | Should Cause Error | 1 / 0             |
        | Should Be Equal    | ${error}           | Division by zero. |
        """
        try:
            self.trigger_transaction(expression)
        except TRXError as err:
            return str(err)
        else:
            raise AssertionError("'%s' should have caused an error."
                                 % expression)
