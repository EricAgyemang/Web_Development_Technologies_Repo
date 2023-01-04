from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
driver.get('https://www.google.com')


#tests that I can input/submit text and see it when the page reloads
class MyTests(TestCase):
	def setup(self):
	    self.browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
	def test_my_feature(self):
	    self.browser.get("http://127.0.0.1:8000")
	    input = self.browser.find_element_by_id("input1")
	    input.send_keys("my input")
	    browser.find_element_by_id("button1").click()
	    browser.implicitly_wait(.5)
	    self.assertContains("my input",self.browser.find_element_by_id("output").text
       #def test_a_unit(self):
         #  pass          

