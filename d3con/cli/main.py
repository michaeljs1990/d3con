"""
Entypoint and setup for the rest of the library
"""
#!/usr/bin/env python
from docopt import docopt
from inspect import getdoc

from d3con.client import Client
from d3con.balance_command import BalanceCommand
from d3con.sell_command import SellCommand

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
        sell        sell coins at a given value on the Poloniex Exchange
    """

    def __init__(self, client):
        doc = getdoc(self)
        arguments = docopt(doc)

        cmd = arguments.get('<COMMAND>')
        if cmd == 'balance':
            balance_cmd = BalanceCommand(client, arguments)
            balance_cmd.run()
        elif cmd == 'sell':
            sell_cmd = SellCommand(client, arguments)
            sell_cmd.run()



def main():
    """
    Entrypoint used in setup.py
    """
    c = Client()
    D3con(c.get_client())
