#!/usr/bin/env python
# encoding: utf-8
import unittest

from ..redisPool import RedisPool
from ..styxQueue import StyxQueue

class StyxQueueTestCase(unittest.TestCase):

	pool = None
	q = None

	def setUp(self):
		hosts = [
			{
				"host": "localhost",
				"port": 6700,
				"db": 1
			},
			{
				"host": "localhost",
				"port": 6701,
				"db": 1
			},
			{
				"host": "localhost",
				"port": 6702,
				"db": 1
			}
		]
		self.pool = RedisPool(hosts)
		sq = StyxQueue(self.pool, "testQ")
		self.q = sq

	def tearDown(self):
		for conn in self.pool.get_all():
			conn.delete("testQ")

	def test_get_name(self):
		qName = self.q.get_name()
		self.assertEqual("testQ", qName)

	def test_put_and_get(self):
		self.q.put("Hello1")
		self.q.put("Hello2")
		self.q.put("Hello3")
		self.q.put("Hello4")

		self.assertEqual("Hello1", self.q.get())
		self.assertEqual("Hello2", self.q.get())
		self.assertEqual("Hello3", self.q.get())
		self.assertEqual("Hello4", self.q.get())
		self.assertIsNone(self.q.get())
		self.assertIsNone(self.q.get())
		self.assertIsNone(self.q.get())
