#!/usr/bin/env python
# encoding: utf-8

class StyxQueue(object):
	pool = None
	name = None

	def __init__(self, redis_pool, queue_name):
		self.pool = redis_pool
		self.name = queue_name

	def get_name(self):
		""" Return the name of this queue """
		return self.name

	def get(self):
		""" Dequeue a message """
		reader = self.pool.get_reader()
		return reader.lpop(self.name)

	def put(self, message):
		""" Enqueue a message """
		writer = self.pool.get_writer()
		return writer.rpush(self.name, message)

	def size(self):
		""" Return the size of the message queue """
		i = 0
		for conn in self.pool.get_all():
			count = conn.llen(self.name)
			i += count
		return i