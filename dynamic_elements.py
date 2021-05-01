import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DynamicElements(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('https://the-internet.herokuapp.com/disappearing_elements')


  def test_name_elements(self):
    driver = self.driver

    options = []
    menu = 5
    tries = 1

    while len(options) < 5:
      options.clear() #Limpiamos la lista en caso de reiniciar el bucle while

      for i in range(menu):
        try:
          option_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
          options.append(option_name.text)
          print(options)
        except: #Entrará aquí si solo encuentra 4 elemetos, ya que range(menu) llega a 5
          print(f'Option number {i + 1} is NOT FOUND')
          tries += 1
          driver.refresh()

    print(f'Finished in {tries} tries')


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)