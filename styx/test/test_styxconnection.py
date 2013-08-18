#!/usr/bin/env python
# encoding: utf-8
import unittest

from ..styxConnection import Styx

class StyxConnectionTestCase(unittest.TestCase):

	hosts = []
	conn = None

	def setUp(self):
		self.hosts = [
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

	def tearDown(self):
		pass
		#for a in self.conn.pool.get_all():
		#	a.delete("testQ")

	def test_get_queue(self):
		conn = Styx(self.hosts)
		q = conn.get_queue("testQ")
		self.assertEqual("testQ", q.get_name())

		q.put("hello")