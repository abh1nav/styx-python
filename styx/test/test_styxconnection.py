#!/usr/bin/env python
# encoding: utf-8
import unittest

from ..styxConnection import Styx

class StyxConnectionTestCase(unittest.TestCase):

	hosts = []
	conn = None

	def setUp(self):
		self.hosts = [
			"localhost:6700",
			"localhost:6701",
			"localhost:6702"
		]
		self.conn = Styx(self.hosts)
		self.q = self.conn.get_queue("testQ")

	def tearDown(self):
		for node in self.conn.pool.get_all():
			node.delete("testQ")

	def test_queue(self):
		self.assertEqual("testQ", self.q.get_name())
		self.q.put("hello")
		self.q.put("world")
		self.assertEqual("hello", self.q.get())

		self.q.put("wat")
		self.assertEqual("world", self.q.get())
		self.assertEqual("wat", self.q.get())