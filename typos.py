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
    driver.get('https://the-internet.herokuapp.com/typos')


  def test_find_typo(self):
    driver = self.driver

    paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
    text_to_check = paragraph_to_check.text
    print(f'Text to check: {text_to_check}')
    print(f'Paragraph to check {paragraph_to_check.text}')

    tries = 1
    found = False
    correct_text = "Sometimes you'll see a typo, other times you won't."

    while text_to_check != correct_text:
      paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
      text_to_check = paragraph_to_check.text
      tries += 1
      driver.refresh()

    while not found:
      if text_to_check == correct_text:
        driver.refresh()
        found = True

    self.assertEqual(found, True)

    print(f'It took {tries} tries to find the typo')


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)