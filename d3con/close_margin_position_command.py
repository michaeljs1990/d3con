"""
Allows you to close your margin position using a bunch
of different methods.. maybe one day anyone. For now I
am just going to add in a way to do a fire sale so you
can dump all your crap. I will also add something a
little more sane which will let you pick a threshold on
both side of your base margin price and sell when one
of them is hit. This is still a little dangerous because
I likely won't have a timmer to say if price is X for Y
minutes to start with so someone very quickly dumping or
buying cause mess with this.
"""
import os

from docopt import docopt
from inspect import getdoc

from d3con.base_command import BaseCommand
from d3con.close_margin.high_low_algo import HighLowAlgo

class CloseMarginPositionCommand(BaseCommand):
    """
    Usage:
        d3con close-margin help
        d3con close-margin hl <pair> <high> <low>

    Options:
        --verbose   Show debug output

    Commands:
        help    you know what this does
        hl      monitor the price and when the high or low price is met close
    """

    def __init__(self, client, args):
        """
        Setup the client little sketch since this is
        a command within a command and you likely dont
        need to parse the args twice.
        """
        super(CloseMarginPositionCommand, self).__init__(client, args)

    def run(self):
        doc = getdoc(self)
        arguments = docopt(doc)

        if arguments.get('help'):
            print doc
        if arguments.get('hl'):
            self.validate(arguments.get('<pair>'))
            high_low_algo = HighLowAlgo(self.client, arguments)
            high_low_algo.run()
