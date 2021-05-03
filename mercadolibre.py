import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #Nos ayudará con las esperas explícitas
from selenium.webdriver.support import expected_conditions as EC

class TestingMercadoLibre(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('https://www.mercadolibre.com/')


  def test_search_ps4(self):
    driver = self.driver

    country = driver.find_element_by_id('CO')
    country.click()

    search_bar = driver.find_element_by_name('as_word')
    search_bar.click()
    search_bar.clear()
    search_bar.send_keys('playstation 4')
    search_bar.submit()
    print('CAMBIÉ DE PÁGINA')
    time.sleep(10)

    """ location = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Bogotá D.C.')))
    location = driver.find_element_by_partial_link_text('Bogotá D.C.')
    location.click()
    #time.sleep(5)

    condition = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Nuevo')))
    condition.click()
    time.sleep(5) """

    order_menu = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, 'andes-dropdown__trigger')))
    order_menu.click()

    higher_price = driver.find_element_by_css_selector('//*[@id="root-app"]/div/div/section/div[1]/div/div/div[2]/div[1]/div/div/div/ul/li[3]/a')
    higher_price.click()
    time.sleep(5)

    ps4_names_and_prices = {}
    for i in range(5):
      product_title = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2')
      product_title_text = product_title.text
      price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/span[1]/span[2]')
      price_text = price.text

      ps4_names_and_prices[product_title_text] = price_text

    print(ps4_names_and_prices)


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)