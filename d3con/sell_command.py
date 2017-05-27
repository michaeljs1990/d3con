"""
https://github.com/s4w3d0ff/python-poloniex/blob/master/poloniex/__init__.py#L365

Above is the general "docs" for the sell command.
"""
import os

class SellCommand(object):
    """
    Risky stuff going on in here. This command lets you
    sell your coins for whatever price you want.
    """

    def __init__(self, client, args):
        """
        Setup the client
        """
        self.client = client

    def run(self):
        """
        Sell a given curreny pair with a market order.
        """

        self.client.sell("LTC/BTC", rate, amount, orderType)
