#!/usr/bin/env python3

import unittest

import classify.py as classify


class TestExclude(unittest.TestCase):

    def test_thoseInRange(self):
        data=[['A',0],['B',5],['C',12],['D',21]]
        c1 = classify.thoseInRange(data,0,20)
        self.assertEqual(c1,[['A',0],['B',5],['C',12]])


if __name__ == '__main__':


    unittest.main()
