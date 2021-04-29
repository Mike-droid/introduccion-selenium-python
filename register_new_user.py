import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class RegisterNewUser(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('http://demo-store.seleniumacademy.com/')


  def test_new_user(self):
    driver = self.driver
    driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click() #Hacemos click en el elemento
    driver.find_element_by_link_text('Log In').click()

    create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
    self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
    create_account_button.click()

    self.assertEqual('Create New Customer Account' , driver.title) #¿El título de la página web es igual al título del driver?

    #Creamos las variables para encontrar los elementos
    first_name = driver.find_element_by_id('firstname')
    middle_name = driver.find_element_by_id('middlename')
    last_name = driver.find_element_by_id('lastname')
    email_address = driver.find_element_by_id('email_address')
    news_letter_suscription = driver.find_element_by_id('is_subscribed')
    password = driver.find_element_by_id('password') #! No utilizar datos reales por la sensibilidad de los datos
    confirm_password = driver.find_element_by_id('confirmation')
    submit_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')

    #Verificamos que los elementos estén habilitados
    self.assertTrue(first_name.is_enabled()
    and middle_name.is_enabled()
    and last_name.is_enabled()
    and email_address.is_enabled()
    and news_letter_suscription.is_enabled()
    and password.is_enabled()
    and confirm_password.is_enabled()
    and submit_button.is_enabled())

    #Pretendemos llenar los campos
    first_name.send_keys('Test')
    middle_name.send_keys('Test')
    last_name.send_keys('Test')
    email_address.send_keys('Test@testingmail.com')
    password.send_keys('Test')
    confirm_password.send_keys('Test')
    news_letter_suscription.click()
    submit_button.click()


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)