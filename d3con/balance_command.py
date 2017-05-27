"""
Include and merge docker-compose configurations into a single file.
Given a docker-compose.yml file, fetch each configuration in the include
section and merge it into a base docker-compose.yml. If any of the included
files have include sections continue to fetch and merge each of them until
there are no more files to include.
"""
import os

from d3con.client import Client

class ValidateCommand(object):
    """
    Check that your credentials work by trying to access
    one of the private API methods.
    """

    def __init__(self, args):
        """
        Setup the client
        """
        wrapper = Client()
        self.client = wrapper.get_client()

    def run(self):
        """
        Check your balances
        """
        print self.client.returnBalances()
