"""
Tor client which enables to run http requests from different IPs.

Example:

    tor = TorClient(password='password')
    session = tor.get_session()
    print("IP:", session.get("http://httpbin.org/ip").text)
    
"""
import time

import requests
from stem import Signal
from stem.control import Controller


class TorClient(object):
    
    def __init__(self, password=None, host='127.0.0.1', port=9050, ctl_port=9051):
        """Creates tor client.
        
        Args:
            password: tor password
            host: tor host
            port: tor socks port 
            ctl_port: tor control port
        """
        self.password = password
        self.host = host
        self.port=port
        self.ctl_port = ctl_port
    
    def _renew_connection(self):
        """Signal tor to switch IP address"""
        with Controller.from_port(port=self.ctl_port) as controller:
            controller.authenticate(password=self.password)
            controller.signal(Signal.NEWNYM)
            while not controller.is_newnym_available():
                time.sleep(controller.get_newnym_wait())

    def get_session(self):
        """Creates a session with a new IP address"""
        self._renew_connection()
        session = requests.session()
        session.proxies = {'http':  'socks5://{}:{}'.format(self.host, self.port), 
                           'https': 'socks5://{}:{}'.format(self.host, self.port)}
        return session
