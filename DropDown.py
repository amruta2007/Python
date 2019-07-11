'''
Created on Jun 9, 2019

@author: facebook
'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
 
 
class Drpdowm(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Firefox()
 
    def test_drpdown(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://www.toolsqa.com/automation-practice-form/')
 
        s1=Select(driver.find_element_by_id('continents'))
 
        print(s1.options)
         
        for opt in s1.options:
            time.sleep(10)
            #s1.select_by_visible_text('Africa')
            s1.select_by_index(2)
            #s1.select_by_value('foo')
            time.sleep(10)
    def tearDown(self):
        self.driver.quit()
 
if __name__ == '__main__':
    unittest.main()