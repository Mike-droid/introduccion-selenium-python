import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_data(file_name):
  rows = []
  data_file = open(file_name, 'r')
  reader = csv.reader(data_file)
  next(reader, None) #Hacemos esto para omitir la cabecera del archivo csv

  for row in reader:
    rows.append(row)
  return rows


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


  @data(*get_data('testdata.csv'))
  @unpack


  def test_search_ddt(self, search_value, expected_count):
    driver = self.driver

    search_field = driver.find_element_by_name('q')
    search_field.clear()
    search_field.send_keys(search_value)
    search_field.submit()

    products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a') #h2 con la clase product-name y adentro hay un ancla

    expected_count = int(expected_count)

    if expected_count > 0:
      self.assertEqual(expected_count, len(products))
    else:
      message = driver.find_element_by_class_name('note-msg')
      self.assertEqual('Your search returns no results.', message)

    print(f'Found {len(products)} products')


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)