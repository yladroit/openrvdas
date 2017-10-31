#!/usr/bin/env python3

import sys
import unittest

sys.path.append('.')

from utils import timestamp

class TestTimestamp(unittest.TestCase):

  def test_timestamp(self):
    self.assertAlmostEqual(timestamp.timestamp(timestamp.time_str()),
                           timestamp.timestamp(), places=1)
    self.assertEqual(timestamp.timestamp('1970-01-01:00:00:10.0'), 10.0)

  def test_time_str(self):
    self.assertEqual(timestamp.time_str(1507810403.33),
                     '2017-10-12:12:13:23.330000')
    self.assertEqual(timestamp.time_str(1507810403.33, time_format='%H/%M'), '12/13')

  def test_date_str(self):
    self.assertEqual(timestamp.date_str(1507810403.33), '2017-10-12')
    self.assertEqual(timestamp.date_str(1507810403.33, date_format='%Y+%j'),
                     '2017+285')

if __name__ == '__main__':
  unittest.main()
