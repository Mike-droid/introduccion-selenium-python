import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Typos(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('https://the-internet.herokuapp.com/tables')


  def test_sort_tables(self):
    driver = self.driver

    table_data = [[] for i in range(5)]
    print(table_data)

    for i in range(5):
      header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
      table_data[i].append(header.text)

      for j in range(4):
        row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]')
        table_data[i].append(row_data.text)

    print(table_data)


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)