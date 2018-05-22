#!/usr/bin/env python3

import unittest
import classify


class TestCheck(unittest.TestCase):

    def test_thoseInRange1(self):
        data=[["A1",1],["B1",2],["C1",7],["D1",10]]
        c1 = classify.thoseInRange(data,0,10)
        self.assertEqual(c1,[["A1",1],["B1",2],["C1",7]])

    def test_thoseInRange2(self):
        data=[["A1",1],["B1",2],["C1",7],["D1",11]]
        c1 = classify.thoseInRange(data,20,30)
        self.assertEqual(c1,["none"])

    def test_thoseNotInRange1(self):
        data=[["A1",1],["B1",2],["C1",7],["D1",10]]
        c1 = classify.thoseInRange(data,20,30)
        self.assertNotEqual(c1,[["A1",1],["B1",2],["C1",7]])

    def test_thoseNotInRange2(self):
        data=[["A1",1],["B1",2],["C1",7],["D1",11]]
        c1 = classify.thoseInRange(data,0,10)
        self.assertNotEqual(c1,["none"])


if __name__ == '__main__':


    unittest.main()
