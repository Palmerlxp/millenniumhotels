'''author: Tina Zhao'''

import unittest
from driver.browser import *
from selenium import webdriver
import time
import logging
from page.Propertypage import PropertyPage



class TestPropertyElements(unittest.TestCase):

    def setUp(self):
        self.driver = chrome_browser()
        self.driver.get("https://www.millenniumhotels.com")
        time.sleep(5)


    def test_property_entrance(self):
        ''' Test proceed to hotel property page'''
        propertypage = PropertyPage(self.driver)

        '''Step1 - Open hotel property page
           Exp1 -  Property page opened '''
        propertypage.proceed_to_propertypage()

        '''Step2 - Check rooms section
           Exp2 -  Property page opened '''
        propertypage.check_rooms_section()


        self.driver.back()



    @unittest.skip("I don't want to run this case.")  #skip one case to keep excuting others
    def test_property_elements(self):
        ''' Test proceed to hotel property page'''
        pass


    def tearDown(self):
        #self.driver.close()  # close broswer tag
        self.driver.quit()     #close broswer


    if __name__ == "__main__":
        unittest.main()
