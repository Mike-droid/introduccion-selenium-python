import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException # Nos servirá como excepción para validar la presencia de un elemento
from selenium.webdriver.common.by import By # Nos ayudará a llamar a las excepciones que queremos validar

class AssertionsTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('http://demo-store.seleniumacademy.com/')


  def test_search_field(self):
    self.assertTrue(self.is_element_present(By.NAME, 'q')) # ¿Existe un elemento con atributo NAME de valor 'q'?


  def test_language_option(self):
    self.assertTrue(self.is_element_present(By.ID, 'select-language')) # ¿Existe un elemento con atributo ID de valor 'select-language'?


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


  def is_element_present(self, how, what): #Verificaremos si un elemento está presente de acuerdo a estos parámetros. "How" indicará el tipo de selectot y "What" el valor que tiene
    try:
      self.driver.find_element(by = how, value = what)
    except NoSuchElementException as variable:
      return False
    return True


if __name__ == '__main__':
  unittest.main(verbosity = 2)