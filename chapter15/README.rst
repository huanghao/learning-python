Networking
==========

`ipaddress <https://docs.python.org/3.4/library/ipaddress.html>`_ - IPv4/IPv6 manipulation library
--------------------------------------------------------------------------------------------------

::

  >>> ipaddress.ip_address('192.168.0.1')
  IPv4Address('192.168.0.1')
  >>> ipaddress.ip_address('2001:db8::')
  IPv6Address('2001:db8::')

  >>> ipaddress.ip_network('192.168.0.0/28')
  IPv4Network('192.168.0.0/28')

  >>> IPv4Address('127.0.0.2') > IPv4Address('127.0.0.1')
  True
  >>> IPv4Address('127.0.0.2') == IPv4Address('127.0.0.1')
  False
  >>> IPv4Address('127.0.0.2') != IPv4Address('127.0.0.1')
  True

  >>> list(ip_network('192.0.2.0/29').hosts())  
  [IPv4Address('192.0.2.1'), IPv4Address('192.0.2.2'),
   IPv4Address('192.0.2.3'), IPv4Address('192.0.2.4'),
   IPv4Address('192.0.2.5'), IPv4Address('192.0.2.6')]

  >>> for addr in IPv4Network('192.0.2.0/28'):
  ...   addr
  ...
  IPv4Address('192.0.2.0')
  IPv4Address('192.0.2.1')
  IPv4Address('192.0.2.2')
  IPv4Address('192.0.2.3')
  IPv4Address('192.0.2.4')
  IPv4Address('192.0.2.5')
  IPv4Address('192.0.2.6')
  IPv4Address('192.0.2.7')
  IPv4Address('192.0.2.8')
  IPv4Address('192.0.2.9')
  IPv4Address('192.0.2.10')
  IPv4Address('192.0.2.11')
  IPv4Address('192.0.2.12')
  IPv4Address('192.0.2.13')
  IPv4Address('192.0.2.14')
  IPv4Address('192.0.2.15')

  >>> IPv4Network('192.0.2.0/28')[0]
  IPv4Address('192.0.2.0')
  >>> IPv4Network('192.0.2.0/28')[15]
  IPv4Address('192.0.2.15')
  >>> IPv4Address('192.0.2.6') in IPv4Network('192.0.2.0/28')
  True
  >>> IPv4Address('192.0.3.6') in IPv4Network('192.0.2.0/28')
  False

socket
------

APIs
~~~~

TCP & UDP

- http, ftp
- arp/rarp, rip, skipy

- socket
- connect
- bind
- listen
- accept
- recv
- send
- close

Multithreading or processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apache

Multiplexing
~~~~~~~~~~~~

Blocking & Non-Blocking

- select
- poll
- epoll
- kqueue

Nginx, NodeJS

http
----

Server

http.server
http.cookie
http.cookiejar

Client

http.client

requests & requests-cache

Twisted
-------

gevent
python-eventlet
tulip(asyncio)
Scrapy
