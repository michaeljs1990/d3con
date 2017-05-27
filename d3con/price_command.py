"""
https://github.com/s4w3d0ff/python-poloniex/blob/master/poloniex/__init__.py#L365

Above is the general "docs" for the sell command.
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

    def inform(self, pair, rate, amnt):
        """
        Log to the commandline the order that you
        are going to make. Mostly useful for logging
        to a file. Should make logging to file the 
        default action in the future and this optional.
        """
        split = pair.split('_')
        print 'Selling {} {} for {} {} each'.format(amnt, split[1], rate, split[0])

    def run(self):
        """
        Sell a given curreny pair with a market order.

        TODO: valid_pairs should be cached.
        """
        pair = self.args.get('<pair>')
        rate = self.args.get('<rate>')
        amnt = self.args.get('<amount>')

        self.validate(pair)
        self.inform(pair, rate, amnt)
        
        self.client.sell(pair, rate, amnt)
