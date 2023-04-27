#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 20:20:25 2023

@author: oliviakusch
"""
import pandas as pd
import unittest
from Group2mvp import annual_grants

projects = pd.read_excel("projects.xlsx")

class TestMethods(unittest.TestCase):
    def test_annual_grants(self):
        expected_result = [1.70528160e+08, 1.16863073e+08, 1.62658791e+08, 1.69989046e+08, 1.99415384e+08, 1.66940380e+08, 1.70481505e+08]
        real_results = annual_grants()
        self.assertEqual(expected_result,real_results)
        
if __name__ == '__main__':
    unittest.main() 