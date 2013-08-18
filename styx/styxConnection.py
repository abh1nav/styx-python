#!/usr/bin/env python
# encoding: utf-8

from styx.redisPool import RedisPool
from styx.styxQueue import StyxQueue

class Styx(object):
	pool = None

	def __init__(self, hostnames, db=0):
		"""
			Creates a Styx connection that manages multiple queues.
			Args:
				hostnames: List of hostnames for the Redis servers. Ex: redis1.example.com, redis2.example.com:1234
				db: The redis db number where queues read and write from.
		"""
		hosts = []
		for url in hostnames:
			conf = {}
			if ":" in url:
				spl = url.split(":")
				conf['host'] = spl[0]
				conf['port'] = int(spl[1])
			else:
				conf['host'] = url
				conf['port'] = 6379
			conf['db'] = db
			hosts.append(conf)

		self.pool = RedisPool(hosts)

	def get_queue(self, name):
		""" Return an instance of StyxQueue with the given name """
		return StyxQueue(self.pool, name)

	def delete_queue(self, queue):
		""" Delete this queue from all registered hosts """
		for host in self.pool.get_all():
			host.delete(queue.get_name())