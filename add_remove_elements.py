import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class AddRemoveElements(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')


  def test_add_remove(self):
    driver = self.driver

    elements_added = int(input('How many elements will you add?: '))
    elements_removed = int(input('How many elements will you remove?: '))
    total_elements = elements_added - elements_removed

    add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

    for i in range(elements_added):
      add_button.click() #Hacemos click en cada botón

    for i in range(elements_removed):
      try:
        #delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
        delete_button = driver.find_element_by_class_name('added-manually')
        delete_button.click()
      except:
        print("You're trying to delete more elements than the existent")
        break

    if total_elements > 0:
      print(f'There are {total_elements} elements on the screen')
    else:
      print(f'There are 0 elements on the screen')


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)