import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class NavigationTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('https://google.com')

  def test_browser_navigation(self):
    driver = self.driver

    search_field = driver.find_element_by_name('q')
    search_field.clear()
    search_field.send_keys('platzi')
    search_field.submit()

    driver.back() #Retroceder en la navegación web
    driver.forward() #Avanzar en la navegación web
    driver.refresh() #Actualizar ventana del navegador


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)