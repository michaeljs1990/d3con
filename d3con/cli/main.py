"""
Entypoint and setup for the rest of the library
"""
#!/usr/bin/env python
from docopt import docopt
from inspect import getdoc

from d3con.balance_command import BalanceCommand

class D3con(object):
    """
    Poloniex command line trading.
    Usage:
        d3con <COMMAND> [--account ACCOUNT]

    Options:
        --account   Account to use from config.yml file 
        --verbose   Show debug output

    Commands:
        validate    check that you can connect to the Poloniex API
    """

    def __init__(self):
        doc = getdoc(self)
        arguments = docopt(doc)

        cmd = arguments.get('<COMMAND>')
        if cmd == 'balance':
            balance_cmd = BalanceCommand(arguments)
            balance_cmd.run()


def main():
    """
    Entrypoint used in setup.py
    """
    D3con()
