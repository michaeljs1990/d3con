"""
List all of your current margin positions
"""
import os

from d3con.base_command import BaseCommand

class ListMarginsCommand(BaseCommand):
    """
    The margins command
    """

    def __init__(self, client, args):
        """
        Setup the client
        """
        super(ListMarginsCommand,self).__init__(client, args)

    def inform(self, positions):
        """
        Print out all non-zero trades
        """
        for market, stats in positions.iteritems():
            if stats.get('liquidationPrice') > 0:
                print '{}: basePrice: {} liquidationPrice: {} gains: {}'.format(market, stats.get('basePrice'), stats.get('liquidationPrice'), stats.get('pl'))

    def run(self):
        """
        Get the last price for a given currency.
        """
        positions = self.client.getMarginPosition()
        self.inform(positions)
        
