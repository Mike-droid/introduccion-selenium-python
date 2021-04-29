import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class CompareProducts(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('http://demo-store.seleniumacademy.com/')


  def test_compare_products_removal_alert(self):
    driver = self.driver
    search_field = driver.find_element_by_name('q')
    search_field.clear() # Limpiamos el texto que haya en la barra de búsqueda, como buena práctica

    search_field.send_keys('tee') #Simulamos que tecleamos 'tee'
    search_field.submit()

    driver.find_element_by_class_name('link-compare').click()
    driver.find_element_by_link_text('Clear All').click()

    alert = driver.switch_to.alert #Como saldra un alert, le decimos al navegador que centre su atención aquí
    alert_text = alert.text

    self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text) #Validamos si el texto del alert es idéntico al que tenemos en la variable

    alert.accept() #Hacemos click en el botón de aceptar


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)