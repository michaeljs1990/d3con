"""
Get the price of a given market
"""
import os

from d3con.base_command import BaseCommand

class PriceCommand(BaseCommand):
    """
    Risky stuff going on in here. This command lets you
    sell your coins for whatever price you want.
    """

    def __init__(self, client, args):
        """
        Setup the client
        """
        super(PriceCommand,self).__init__(client, args)

    def inform(self, pair, m):
        """
        Log to the commandline the order that you
        are going to make. Mostly useful for logging
        to a file. Should make logging to file the 
        default action in the future and this optional.
        """
        print '{}: current: {} low: {} high: {}'.format(pair, m.get('last'), m.get('low24hr'), m.get('high24hr'))

    def run(self):
        """
        Get the last price for a given currency.
        """
        pair = self.args.get('<pair>')

        self.validate(pair)
        market = self.client.returnTicker()
        self.inform(pair, market.get(pair))
        
