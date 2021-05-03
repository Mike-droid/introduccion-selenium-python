import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from google_page import GooglePage #Nos estamos trayendo la clase del otro archivo

class GoogleTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)


  def test_search(self):
    google = GooglePage(self.driver)
    google.open()
    google.search('Platzi')

    self.assertEqual('Platzi', google.keyword)


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)