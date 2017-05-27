"""
Get credentials to connect to the Poloniex API
"""
#!/usr/bin/env python
import os
import yaml

from poloniex import Poloniex

class Client(object):
    """
    Basic wrapper around Poloniex auth
    """

    def __init__(self):
        conf = self.open_config() 
        self.p = Poloniex()
        self.p.key = conf['michael']['key'] 
        self.p.secret = conf['michael']['secret']

    def open_config(self):
        """
        Load yaml from disk given a file name and
        turn it into a python dict for manipulation
        Keyword arguments:
            file_name -- file name to fetch yaml from
        """
	base_path = os.environ['HOME']
        conf_path = '.config/d3con/config.yml'

        with open(os.path.join(base_path, conf_path), "r") as stream:
            try:
                conf = yaml.load(stream)
            except yaml.YAMLError as exc:
                print exc
                exit(1)

        return conf

    def get_client(self):
        """
        Return the poloniex client that this is wrapping
        after the keys have already been setup.
        """
        return self.p
