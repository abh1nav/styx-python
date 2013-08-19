styx: A simple distributed message queue based on Redis
=======================================================

Styx is a simple library that turns a bunch of standalone `Redis <http://redis.io/>`_ servers into a powerful distributed queue.
The redis servers don't need any special configuration or even be aware of each other in any way. The messages are loosely ordered.
A java version can be found `here <https://github.com/abh1nav/styx/>`_. The java and python versions are compatible - i.e. messages
published by one client can be read by the other client.

Install
-------
.. code-block:: python

    pip install styx

Quickstart
----------

.. code-block:: python

    #!/usr/bin/env python
    # encoding: utf-8

    import styx

    # Define the Redis host locations (the default port is 6379)
    hosts = [ "redis1.example.com", "redis2.example.com:8080", "redis3.example.com" ]

    connection = styx.Styx(hosts, db=3) # default db is 0
    # If a queue doesn't exist, it will be created automatically
    q = connection.get_queue("myTestQueue")
    q.put("Hello")
    q.put("World")
    q.put("Message1234")

    q.get() # returns "Hello"
    q.get() # returns "World"

    # Check how many messages are left in the queue
    q.size() # returns 1

    # Delete this queue
    connection.delete_queue(q)

Unit Tests
----------
To run unit tests, make sure you have 3 redis instances running on localhost at ports 6700, 6701, 6702.

.. code-block:: shell

    pip install nose
    nosetests


Source available on GitHub: http://github.com/abh1nav/styx-python/