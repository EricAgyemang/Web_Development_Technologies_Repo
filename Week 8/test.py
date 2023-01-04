from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#driver.get('https://www.illinoisstate.edu')

#The site I am using is Illinois state university Redbird card website 

class RedBirdCardForm(unittest.TestCase):
      """
      User Story:
    
      As a list author, I need to test that I can input/submit my details to the redbird account for 
      refund and see when the page reloads

      AC: input can be added then retrieved
      """

      @classmethod
      def setUpClass(self):
          self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
          self.driver.get('https://forms.illinoisstate.edu/forms/refund')
      
      
      def test_fill_biodata_form(self):
          first_name = self.driver.find_element(By.ID, 'field40394474-first') 
          first_name.send_keys('Eric')  
          
          last_name = self.driver.find_element(By.ID, 'field40394474-last')
          last_name.send_keys('Agyemang')
          
          uid = self.driver.find_element(By.ID, 'field40394519') 
          uid.send_keys('803686944')  

      
      def test_fill_reasons_form(self):          
          withdrawal_reason = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Graduation')]")
          print(withdrawal_reason.is_selected())
          withdrawal_reason.click()
                 
          
      def test_fill_contact_form(self):
          email_address = self.driver.find_element(By.ID, 'field99222880')
          email_address.send_keys('eagyem2@ilstu.edu')  
          
          email_address_confirmation = self.driver.find_element(By.ID, 'field99222880_confirm')
          email_address_confirmation.send_keys('eagyem2@ilstu.edu') 
          
          address_to_mail_refund = self.driver.find_element(By.ID, 'field40394845-address')
          address_to_mail_refund.send_keys('320 W Locust St.') 
                
          city = self.driver.find_element(By.ID, 'field40394845-city')
          city.send_keys('Normal') 
          
          zip_code = self.driver.find_element(By.ID, 'field40394845-zip')
          zip_code.send_keys('61761') 
                    
      
      def test_varificarion(self):     
          text_area = self.driver.find_element(By.ID, 'field40431009')
          text_area.send_keys('Please refund my Redbird Account balance into my checking account stored on file.\nThank you!') 
          
          
          verification = self.driver.find_element(By.XPATH, "//*[contains(text(), 'By checking this box, you are affirming that you are the person named above and understand that the refund will be processed through Student Accounts.')]")
          print(verification.is_selected())
          verification.click()
          
          self.driver.implicitly_wait(.5)
                   

if __name__ == '__main__':
    unittest.main()





