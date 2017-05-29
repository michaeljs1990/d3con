""" This is a real, real dumb command that simply polls for
the current price of your position and when your high or
low demand is met dump on the market. high or low can also
provide some peace of mind for people who would rather not
be cashed out automatically because they are about to default
on the loan.
"""
import os
import time

from d3con.base_command import BaseCommand

class HighLowAlgo(BaseCommand):
    """
    Same as comment above.. stupid pep8
    """

    def __init__(self, client, args):
        """
        Setup the client little sketch since this is
        a command within a command and you likely dont
        need to parse the args twice.
        """
        super(HighLowAlgo, self).__init__(client, args)

    def execute(self, pair, ceil, floor):
        """
        Loop until condition is met and execute order when it is.
        Sleep for 4 seconds since the API seems to cache calls for
        this time period anyway and no reason to kill it.
        """
        ceilf = float(ceil)
        floorf = float(floor)
        while True:
            markets = self.client.returnTicker()
            price = float(markets.get(pair).get('last'))
            if (price >= ceilf) or (price <= floorf):
                self.client.closeMarginPosition(pair)
                break
            print "price: {:.8f} cieling: {:.8f} floor: {:.8f}".format(price, ceilf, floorf)
            time.sleep(4)

    def run(self):
        pair = self.args.get('<pair>')
        ceiling = self.args.get('<high>')
        floor = self.args.get('<low>')
        self.execute(pair, ceiling, floor)
