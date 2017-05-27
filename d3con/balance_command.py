"""
Get the given balance of your account. This is not
yet able to be configured but has what I believe to
be a sane default. If will not show you any of your
balances that are zero since poloniex supports some
100 coins or so.
"""
import os

from d3con.base_command import BaseCommand

class BalanceCommand(BaseCommand):
    """
    Check that your credentials work by trying to access
    one of the private API methods.
    """

    def __init__(self, client, args):
        """
        Setup the client
        """
        super(BalanceCommand, self).__init__(client, args)

    def run(self):
        """
        Check your balances and filter out accounts that are empty
        """
        for coin, price in self.client.returnBalances().iteritems():
            if price != '0.00000000': print coin + ": " + price
