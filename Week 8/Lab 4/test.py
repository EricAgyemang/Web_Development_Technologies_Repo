import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#driver.get('https://www.illinoisstate.edu')

#I want to test that I can input/submit a name to search for it and see when the page reloads

class MyTests(unittest.TestCase):

    """
    As a data scientist, I need to search for the list of data scientist under 'people' on linkedIn  
    who have the surname 'Agyemang' and then go through the list to make a choice of personnel by 
    entering his/her first name and go through his/her profile.
    
    AC: retieve a list of data scientist from linkedIn professional archieve.
        Recieve a special message from an empty list
    """
    
    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.browser.get("https://www.linkedin.com/pub/dir?firstName=Eric&lastName=&trk=people-guest_people-search-bar_search-submit")
        
    def test_search_by_text(self):
        input = self.browser.find_element_by_class("input1").click()
        input.send_keys("my input")
	input.send_keys(driver.ENTER)
      #  self.input.submit()
        browser.implicitly_wait(.5)
        lists = self.browser.find_element_by_last_name("Agyemang")
        self.assertEqual(8,len(lists))

    def test_search_by_name(self):
        input= self.browser.find_element_by_id("input2")
        input.send_keys("my input")
        self.input.submit()
        browser.implicitly_wait(.5)
        myNewList = self.browser.find_element_by_first_name("Eric")
        self.assertEqual(4,len(myNewList))

if __name__ == '__main__':
    unittest.main()




