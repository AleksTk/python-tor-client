# Python Tor Client

Enables to run http requests over Tor.

## Usage

```
    print("Default IP:", requests.get("http://httpbin.org/ip").text)
    >>> 185.170.42.18

    tor = TorClient(password='password')
    
    session = tor.get_session()  # get new identity
    print("IP:", session.get("http://httpbin.org/ip").text)
    >>> 171.25.193.20
    
    session = tor.get_session()  # get new identity
    print("IP:", session.get("http://httpbin.org/ip").text)
    >>> 192.42.116.16
```

## Installing Tor on Windows
```
tor --service install -options ControlPort 9051
```

## License

MIT License

Copyright (c) 2017 Alexander Tkachenko
