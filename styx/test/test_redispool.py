#!/usr/bin/env python
# encoding: utf-8
import unittest

from ..redisPool import RedisPool

class RedisPoolTestCase(unittest.TestCase):

	pool = None

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

	def tearDown(self):
		""" Delete the test config file at test_config_path """
		del self.pool

	def  test_get_reader(self):
		""" Check if the RedisPool#getReader call returns readers in the correct order """
		reader = self.pool.get_reader()
		self.assertIsNotNone(reader)

		self.pool.get_reader()
		self.pool.get_reader()
		reader2 = self.pool.get_reader()
		self.assertEqual(reader, reader2)

		self.assertEqual(3, len(self.pool.readers))

	def test_get_writer(self):
		""" Check if the RedisPool#getWriter call returns writers in the correct order """
		writer = self.pool.get_writer()
		self.assertIsNotNone(writer)

		self.pool.get_writer()
		self.pool.get_writer()
		writer2 = self.pool.get_writer()
		self.assertEqual(writer, writer2)

		self.assertEqual(3, len(self.pool.writers))

	def test_get_size(self):
		""" Check if the RedisPool#getSize returns the correct size """
		size = self.pool.get_size()
		self.assertEquals(3, size)