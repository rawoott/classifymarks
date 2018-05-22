#!/usr/bin/env python3

import unittest
import classify


class TestCheck(unittest.TestCase):

    def test_thoseInRange1(self):
        data=[["A1",1],["B1",2],["C1",7],["D1",11]]
        c1 = classify.thoseInRange(data,0,10)
        self.assertEqual(c1,[["A1",1],["B1",2],["C1",7]])


if __name__ == '__main__':


    unittest.main()
