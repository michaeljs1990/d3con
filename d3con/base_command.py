"""
https://github.com/s4w3d0ff/python-poloniex/blob/master/poloniex/__init__.py#L365

Above is the general "docs" for the sell command.
"""
import os

class BaseCommand(object):
    """
    Risky stuff going on in here. This command lets you
    sell your coins for whatever price you want.
    """

    def __init__(self, client, args):
        """
        Setup the client
        """
        self.client = client
        self.args = args

    def validate(self, pair):
        """
        Check if you are passing in a valid pair.
        Should make this better so it tells you to
        run another command to see what all the valid
        pairs are.
        """
        if pair not in self.client.returnTicker():
            print pair + " is not a valid pair."
            exit(1)
