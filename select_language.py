import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select #Así podremos elegir las opciones de un dropdown

class LanguageOptions(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('http://demo-store.seleniumacademy.com/')


  def test_select_language(self):
    exposed_options = ['English', 'French', 'German'] # Los lenguajes disponibles de la página web, en ese orden
    active_options = []

    select_language = Select(self.driver.find_element_by_id('select-language'))

    self.assertEqual(3, len(select_language.options))

    for option in select_language.options:
      active_options.append(option.text) #Agregamos el texto a la lista

    self.assertListEqual(exposed_options, active_options) # Comparamos ambas listas, si son idénticas, la prueba pasará

    self.assertEqual('English', select_language.first_selected_option.text) #Verificamos que 'English' es la primera opción por defecto

    select_language.select_by_visible_text('German') #Verificamos que existe la opción con texto 'German'

    self.assertTrue('store=german' in self.driver.current_url) #Esta es parte de la URL con idioma en alemán

    select_language = Select(self.driver.find_element_by_id('select-language'))
    select_language.select_by_index(0) #Índex 0 es English, 1 es French y 2 es German


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)