import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Search_Tests(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('http://demo-store.seleniumacademy.com/')


  def test_search_tee(self):
    driver = self.driver
    search_field = driver.find_element_by_name('q')
    search_field.clear() #Limpiará el campo de búsqueda en caso de que haya algún texto
    search_field.send_keys('tee') #Simulamos que escribimos 'tee' (camisa en inglés)
    search_field.submit() #Envía los datos


  def test_search_salt_shaker(self):
    driver = self.driver
    search_field = driver.find_element_by_name('q')
    search_field.send_keys('salt shaker')
    search_field.submit()

    products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
    self.assertEqual(1, len(products))


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)