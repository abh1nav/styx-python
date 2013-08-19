#!/usr/bin/env python
# encoding: utf-8

from threading import RLock

import redis

class RedisPool(object):

	all_connections = None
	readers = None
	writers = None
	rlock = None
	wlock = None

	def __init__(self, hosts):
		""" Initialize all internal fields """
		all_connections = list()
		self.readers = list()
		self.writers = list()
		self.rlock = RLock()
		self.wlock = RLock()

		for h in hosts:
			r = redis.StrictRedis(host=h['host'], port=h['port'], db=h['db'])
			all_connections.append(r)
			self.readers.append(r)
			self.writers.append(r)

		self.all_connections = tuple(all_connections)

	def get_reader(self):
		"""" Return a connection that's eligible for a read """
		self.rlock.acquire()
		try:
			conn = self.readers[0]
			self.readers.remove(conn)
			self.readers.append(conn)
		finally:
			self.rlock.release()
		return conn

	def get_writer(self):
		""" Return a connection that's eligible for a write """
		self.wlock.acquire()
		try:
			conn = self.writers[0]
			self.writers.remove(conn)
			self.writers.append(conn)
		finally:
			self.wlock.release()
		return conn

	def get_all(self):
		""" Return a list of all connections """
		return self.all_connections

	def get_size(self):
		""" Return the number of active connections in the pool """
		return len(self.all_connections)