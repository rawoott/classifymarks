#!/usr/bin/env python3

import unittest
import classify


class TestCheck(unittest.TestCase):

    def test_thoseInRange1(self):  #simple test to check if it includes all the values except 10(the upper value)
        data=[["A1",1],["B1",2],["C1",7],["D1",10]]  
        c1 = classify.thoseInRange(data,0,10)
        self.assertEqual(c1,[["A1",1],["B1",2],["C1",7]])  

    def test_thoseInRange2(self):  #test to check if none is produced if no values in range
        data=[["A1",1],["B1",2],["C1",7],["D1",11]]
        c1 = classify.thoseInRange(data,20,30)
        self.assertEqual(c1,["none"])

    def test_thoseNotInRange1(self): #test to check if values are not in range it does not store values
        data=[["A1",1],["B1",2],["C1",7],["D1",10]]  
        c1 = classify.thoseInRange(data,20,30)
        self.assertNotEqual(c1,[["A1",1],["B1",2],["C1",7]])

    def test_thoseNotInRange2(self):  #test to check incorrect data does not give store correct values
        data=[["A1",1],["B1",2],["C1",7],["D1",11]]
        c1 = classify.thoseInRange(data,0,10)
        self.assertNotEqual(c1,["none"])
#tests chosen from lab examples
    def test_Lab1(self):
        data=[["A",0],["B",49],["C",59],["D",60],["E",69],["F",74],["H",100]]
        c1 = classify.thoseInRange(data,70,75)
        self.assertEqual(c1,[["F",74]])

    def test_Lab2(self):
        data=[["A",0],["B",49],["C",59],["D",60],["E",69],["F",74],["H",100]]
        c1 = classify.thoseInRange(data,0,49)
        self.assertEqual(c1,[["A",0]])

    def test_Lab3(self):
        data=[["A",0],["B",49],["C",59],["D",60],["E",69],["F",74],["H",100]]
        c1 = classify.thoseInRange(data,61,69)
        self.assertEqual(c1,["none"])



if __name__ == '__main__':


    unittest.main()
