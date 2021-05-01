import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DynamicControls(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('https://the-internet.herokuapp.com/dynamic_controls')


  def test_addRemoveCheckBox(self):
    driver = self.driver

    #Conseguir los elemetos
    check_box = driver.find_element_by_css_selector('#checkbox')
    add_remove_button = driver.find_element_by_css_selector('#checkbox-example > button')

    #Interactuar con los elementos
    check_box.click()
    add_remove_button.click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox')))
    add_remove_button.click()


  def test_write_in_input_field(self):
    driver = self.driver

    #Conseguir los elemetos
    enable_disable_button = driver.find_element_by_css_selector('#input-example > button')
    input_field = driver.find_element_by_css_selector('#input-example > input[type=text]')

    #Interactuar con los elementos
    enable_disable_button.click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))
    input_field.clear() #En caso de que tenga texto escrito
    input_field.send_keys('Platzi')
    enable_disable_button.click()


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)