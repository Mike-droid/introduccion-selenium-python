import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@ddt
class searchDDT(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('http://demo-store.seleniumacademy.com/')


  @data(('dress', 5), ('music', 5)) #Creamos 2 tuplas
  @unpack


  def test_search_ddt(self, search_value, expected_count):
    driver = self.driver

    search_field = driver.find_element_by_name('q')
    search_field.clear()
    search_field.send_keys(search_value)
    search_field.submit()

    products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a') #h2 con la clase product-name y adentro hay un ancla
    print(f'Found {len(products)} products')

    for product in products:
      print(product.text)

    self.assertEqual(expected_count, len(products))


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)