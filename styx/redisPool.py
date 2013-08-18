#!/usr/bin/env python
# encoding: utf-8
import redis

class RedisPool(object):

	all_connections = None
	readers = None
	writers = None

	def __init__(self, hosts):
		""" Initialize all internal fields """
		self.all_connections = list()
		self.readers = list()
		self.writers = list()
		for h in hosts:
			r = redis.StrictRedis(host=h['host'], port=h['port'], db=h['db'])
			self.all_connections.append(r)
			self.readers.append(r)
			self.writers.append(r)

	def get_reader(self):
		"""" Return a connection that's eligible for a read """
		conn = self.readers[0]
		self.readers.remove(conn)
		self.readers.append(conn)
		return conn

	def get_writer(self):
		""" Return a connection that's eligible for a write """
		conn = self.writers[0]
		self.writers.remove(conn)
		self.writers.append(conn)
		return conn

	def get_all(self):
		""" Return a list of all connections """
		return self.all_connections

	def get_size(self):
		""" Return the number of active connections in the pool """
		return len(self.all_connections)