from tor_client import TorClient
import requests

print("Default IP:", requests.get("http://httpbin.org/ip").text)

tor = TorClient()

session = tor.get_session()  # get new identity
print("New IP:", session.get("http://httpbin.org/ip").text)

session = tor.get_session()  # get new identity
print("New IP:", session.get("http://httpbin.org/ip").text)