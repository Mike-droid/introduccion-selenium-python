# Curso de Introducción a Selenium con Python

## Conocer el ecosistema de Selenium

### Bienvenida al curso

### Historia de Selenium

¿Qué es selenium?: Es una suite de heramientas para **automatización** de navegadores.

Selenium es compatbile con los navegadores web más populares y algunos lenguajes de programación; Java, C#, Kotlin, Perl, Php, Python, Ruby, JavaScript.

**Importante**: Selenium **NO** es una herramienta de testing ni web scraping (aunque se puede usar para esto, no es su enfoque).

Para este curso, cuando mencionemos "Selenium" nos estaremos refiriendo específicamente a [Selenium WebDriver](https://www.selenium.dev/).

*Dato curioso*: El origen del nombre es por "Selenio", que es medicina para el envenenamiento por mercurio.

**Importante**: Selenium **NO** es un software, sino una suite de distintos softwares.

Pros de Selenium IDE:

- Excelente para iniciar en Testing y Pruebas unitarias
- No requiere saber programar
- Exporta scripts para Selenium RC y Selenium WebDriver
- Genera reportes

Contras de Selenium IDE:

- Disponible solo para Firefox y Chrome
- No sorporta DDT (Data Driven Testing)

Pros de Selenium RC:

- Soporte para:
  - Varias plataformas, navegadores y lenguajes
  - Operaciones lógicas y condicionales
  - DDT
- Posee una API madura

Contras de Selenium RC:

- Complejo de instalar
- Necesita de un servidor corriendo
- Comandos redundants y ambigüos en su API
- Navegación no tan realista

Pros de Selenium WebDriver:

- Soporte para múltiples lenguajes
- Fácil de instalar
- Comunicación directa con el navegador
- Interacción más realista

Constras de Selenium WebDriver:

- No soporta nuevos navegadores tan rápido
- No genera reportes o resultados de pruebas
- Requiere de saber programar (Pero con Platzi esto no es desventaja (; )

Sobre Selenium Grid:

- Se utiliza junto a Selenium RC
- Permite correr pruebas en paralelo
- Conveniente para ahorrar tiempo

### Otras herramientas de testing y automatización

- [Puppeteer](https://pptr.dev/)
- [Cypress.io](https://www.cypress.io/)

Ninguna es mejor que la otra, todo depende de tus necesidades y condiciones.

## Preparar entorno de trabajo

### Configurar entorno de trabajo

Deberemos instalar:

- [Python](https://www.python.org/downloads/)
- Selenium -> En la terminal (tipo unix) `pip3 install selenium`
- PyUnitReport -> En la terminal (tipo unix) `pip3 install pyunitreport`

### Hola mundo

Cosas importantes de Unittest (PyTest)

- *Test Fixture*: preparaciones para antes y después de la prueba
- *Test Case*: unidad de código a probar
- *Test Suite*: colección de Test Cases
- *Test Runner*: orquestador de la ejecución
- *Test Report*: resumen de resultados

#### Creando entorno virtual en python 3.8

1. Instalar: `sudo apt-get install python3.8-venv`
2. Ejecutar: `sudo python3.8 -m venv nombreDelProyecto`
3. Crear alias: `alias avenv="source venv/bin/activate"` (venv es el nombre del proyecto)
4. Ejecutar alias: `avenv`

[Para instalar Chrome en Ubuntu 20.04](https://linuxize.com/post/how-to-install-google-chrome-web-browser-on-ubuntu-20-04/)

`wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`

`sudo apt install ./google-chrome-stable_current_amd64.deb`

[Para instalar chromium driver en Ubuntu](https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/)

***IMPORTANTE***: Para poder instalar con pip las librerías solamente en el entorno virutal de Python, hay que modificar el archivo "pyvenv.cfg"

```python
home = /usr/bin
include-system-site-packages = true #!debe estar en true
version = 3.8.5
```

Si no deja modificar, ejecutar: `sudo chown -r nombre_de_usuario directorio_del_proyecto`, en mi caso fue: `sudo chown -r mike_angel_rm /home/mike_angel_rm/personalProjects/CursoIntroduccionSeleniumPython`

Apagamos el entorno virtual y lo volvemos a encender. Instalamos las librerías.

Si el código no funciona, esto funcionó para mí en WSL2:

hello_world.py:

```python
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class HelloWorld(unittest.TestCase):

  @classmethod
  def setUpClass(cls): # Qué es lo que se va a hacer
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options) #Ruta de driver en unix
    driver = cls.driver # Para no tener que escribir self driver en cada línea
    #driver.implicity_wait(10)


  def test_hello_world(self):
    driver = self.driver
    driver.get('https://www.platzi.com')


  def test_visit_wikipedia(self):
    driver = self.driver
    driver.get('https://www.wikipedia.org')


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit() # Cerramos la ventana del navegador después de cada prueba


if __name__ == '__main__':
  # output es el nombre del reporte
  unittest.main(verbosity=2 , testRunner= HTMLTestRunner(output = 'reportes', report_name='hello-world-report'))
```

Es ***importante*** tener chrome/chromium y chromedriver instalados en WSL2.

## Utilizar comandos básicos

### Encontrar elementos con find_element

En Selenium, podemos usar los selectores de las páginas web para llegar a los elementos, como son:

- ID
- Nombre del atributo
- Nombre de la clase
- Nombre de la etiqueta
- XPath -> Ruta de nodos en XML que indica la ubicación exacta de dónde se encuentra un elemento. NO es la mejor opción, pues los elementos de una página web pueden cambiar.
- Selector de CSS
- Texto del link
- Texto parcial del link

Podemos practicar en [Madison Island](http://demo-store.seleniumacademy.com/) (Es un e-commerce falso para practicar).

Instrucciones usadas en esta clase:

- `self.driver.find_element_by_id` -> Encontrar elemento por su ID
- `self.driver.find_element_by_name` -> Encontrar elemento por su name
- `self.driver.find_element_by_class_name` -> Encontrar elemento por nombre de clase CSS
- `find_elements_by_tag_name` -> Encontrar elementos por sus etiquetas HTML
- `self.driver.find_element_by_xpath` -> Encontrar elemento por su XPATH
- `self.driver.find_element_by_css_selector` -> Encontrar elemento por su selector CSS

Código de la clase (en WSL):

search_test.py

```python
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class HelloWorld(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('http://demo-store.seleniumacademy.com/')
    #driver.maximize_window()
    #driver.implicitly_wait(15) # segundos


  def test_search_text_fild(self):
    search_field = self.driver.find_element_by_id("search")


  def test_search_text_field_by_name(self):
    search_field = self.driver.find_element_by_name("q")


  def test_search_text_field_class_name(self):
    search_field = self.driver.find_element_by_class_name("input-text")


  def test_search_button_enabled(self):
    button = self.driver.find_element_by_class_name("button")


  def test_count_of_promo_banner_images(self):
    banner_list = self.driver.find_element_by_class_name("promos") #Buscamos la clase "promos"
    banners = banner_list.find_elements_by_tag_name("img") #Buscamos las etiquetas img dentro de promos
    self.assertEqual(3, len(banners)) #Hacemos una assertion para ver si efectivamente es la cantidad de imágenes que esperamos
    #! NO son 3 imágenes, son 4, pero recordemos que se cuenta: [0,1,2,3]


  def test_vip_promo(self):
    vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')


  def test_shopping_cart(self):
    shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)
```

### Preparar assertions y test suites

Con estos 2 elementos podemos hacer pruebas que sean más efectivas.

*Assertions*: Son métodos que permiten validar un valor esperado en la ejecución del test. Si el resultado es verdadero el test continúa, en caso contrario "falla" y termina. Ejemplo: `assertEqual(price.text, "300")`

*Test Suites*: Colección de test unificados en una sola prueba, permitiendo tener resultados grupales e individuales.

[PDF de métodos de Selenium](https://static.platzi.com/media/public/uploads/archivo_complementario_assertions_test_suites_e4ace318-3bc2-47e1-8c39-a3bdeed25f48.pdf)

Tenemos creados los archivos "assertions.py" y "searchTests.py". Creamos un nuevo archivo para ejecutar ambas pruebas en paralelo, se llamará "smoke_test.py"

assertions.py:

```python
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException # Nos servirá como excepción para validar la presencia de un elemento
from selenium.webdriver.common.by import By # Nos ayudará a llamar a las excepciones que queremos validar

class AssertionsTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('http://demo-store.seleniumacademy.com/')


  def test_search_field(self):
    self.assertTrue(self.is_element_present(By.NAME, 'q')) # ¿Existe un elemento con atributo NAME de valor 'q'?


  def test_language_option(self):
    self.assertTrue(self.is_element_present(By.ID, 'select-language')) # ¿Existe un elemento con atributo ID de valor 'select-language'?


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


  def is_element_present(self, how, what): #Verificaremos si un elemento está presente de acuerdo a estos parámetros. "How" indicará el tipo de selectot y "What" el valor que tiene
    try:
      self.driver.find_element(by = how, value = what)
    except NoSuchElementException as variable:
      return False
    return True


if __name__ == '__main__':
  unittest.main(verbosity = 2)
```

searchTests.py:

```python
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Search_Tests(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('http://demo-store.seleniumacademy.com/')


  def test_search_tee(self):
    driver = self.driver
    search_field = driver.find_element_by_name('q')
    search_field.clear() #Limpiará el campo de búsqueda en caso de que haya algún texto
    search_field.send_keys('tee') #Simulamos que escribimos 'tee' (camisa en inglés)
    search_field.submit() #Envía los datos


  def test_search_salt_shaker(self):
    driver = self.driver
    search_field = driver.find_element_by_name('q')
    search_field.send_keys('salt shaker')
    search_field.submit()

    products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
    self.assertEqual(1, len(products))


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)
```

smoke_test.py:

```python
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchTests import Search_Tests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest) # Nombre de la clase de prueba
search_test = TestLoader().loadTestsFromTestCase(Search_Tests) # Nombre de la clase de prueba

# Construyendo suite de pruebas
smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
  "output": "smoke-report"
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
```

### Entender las clases WebDriver y WebElement

Como viste en clases anteriores, un sitio web se construye por código HTML en forma de árbol, conteniendo distintos elementos con los que podemos interactuar según estén presentes o no en nuestra interfaz gráfica.

Selenium WebDriver nos brinda la posibilidad de poder referirnos a estos elementos y ejecutar métodos específicos para realizar las mismas acciones que un humano haría sobre los mismos, gracias a las clases WebDriver y WebElement.

#### Clase WebDriver

Cuenta con una serie de propiedades y métodos para interactuar directamente con la ventana del navegador y sus elementos relacionados, como son pop-ups o alerts. Por ahora nos centraremos a las más utilizadas.

#### Propiedades de la clase WebDriver

Estas son las más comunes para acceder al navegador.

Propiedad/Atributo|Descripción|Ejemplo
|---|---|---|
current_url|Obtiene la URL del sitio en la que se encuentra el navegador|driver.get_url
current_window_handle|Obtiene la referencia que identifica a la ventana activa en ese momento|driver.current_window_handle
name|Obtiene el nombre del navegador subyacente para la instancia activa|driver.name
orientation|Obtiene la orientación actual del dispositivo móvil|driver.orientation
page_source|Obtiene el código fuente de disponible del sitio web|driver.page_source
title|Obtiene el valor de la etiqueta `<title>` del sitio web|driver.title

#### Clase WebElement

Esta clase nos permite interactuar específicamente con elementos de los sitios web como textbox, text area, button, radio button, checkbox, etc.

#### Propiedades más comunes de la clase WebElement

Propiedad/Atributo|Descripción|Ejemplo
|---|---|---|
size|Obtiene el tamaño del elemento|login.size
tag_name|Obtiene el nombre de la etiqueta HTML del elemento|login.tag_name
text|Obtiene el texto del elemento|login.text

#### Métodos más comunes de la clase WebElement

Propiedad/Atributo|Descripción|Ejemplo
|---|---|---|
clear()|Limpia el contenido de un textarea|first_name.clear()
click()|Hace clic en el elemento|send_button.click()
get_attribute(name)|Obtiene el valor del atributo de un elemento|submit_button.get_attribute(‘value’) last_name.get_attribute(max_length)
is_displayed()|Verifica si el elemento está a la vista al usuario|banner.is_displayed()
is_enabled()|Verifica si el elemento está habilitado|radio_button.is_enabled()
is_selected()|Verifica si el elemento está seleccionado, para el caso de checkbox o radio button|checkbox.is_selected()
send_keys(value)|Simula escribir o presionar teclas en un elemento|email_field.send_keys(‘team@platzi.com’)
submit()|Envía un formulario o confirmación en un text area|search_field.submit()
value_of_css_property(property_name)|Obtiene el valor de una propiedad CSS del elemento|header.value_of_css_property(‘background-color’)

## Interactuar con elementos

### Manejar form, textbox, chckbox y radio button

Pudimos simular un registro de un usuario en la página con el siguiente código:

register_new_user.py:

```python
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
```

### Manejar dropdown y listas

Lo que hicismos en esta clase fue tomar las opciones de un dropdown:

select_language.py:

```python
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
```

### Manejar alert y pop-up

En esta clase logramos obtener el texto de un alert y cerrarlo.

alerts.py:

```python
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
```

### Automatizar navegación

[23 comandos esenciales de Selenium WebDriver](https://www.techbeamers.com/important-selenium-webdriver-commands/)

En esta clase pudimos navegar en la web de manera automática

automatic_navigation.py

```python
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class NavigationTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('https://google.com')

  def test_browser_navigation(self):
    driver = self.driver

    search_field = driver.find_element_by_name('q')
    search_field.clear()
    search_field.send_keys('platzi')
    search_field.submit()

    driver.back() #Retroceder en la navegación web
    driver.forward() #Avanzar en la navegación web
    driver.refresh() #Actualizar ventana del navegador


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)
```

## Sincronizar pruebas

### Demora implícita y explícita

Las pausas son buenas para el asincronismo.

Tenemos 2 tipos de demoras en Selenium:

- Implícita: busca uno o varios elementos en el DOM si no se encuentran disponibles por la cantidad de tiempo asignado. -> Ejemplo: `implicitly_wait(10)`
- Explícita: utiliza condiciones de espera determinados y continúa hasta que se cumplan.

### Condicionales esperadas

[PDF con Condicionales esperadas](https://static.platzi.com/media/public/uploads/archivo_complementario_condicionales_esperadas_7204dca9-869e-4e49-a1a6-43e0c0c224e8.pdf)

waits.py:

```python
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #Nos ayudará con las esperas explícitas
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWaitTests(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('http://demo-store.seleniumacademy.com/')


  def test_account_link(self):
    WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')
    # esperará 10 segundos hasta que se cumpla la condición, está en una lambda function

    account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
    account.click()

  def test_create_new_customer(self):
    self.driver.find_element_by_link_text('ACCOUNT').click()

    my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
    my_account.click()

    create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
    create_account_button.click()

    WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)
```

### Condicionales esperadas, tabla

Expected Condition|Descripción|Ejemplo
---|---|---
element_to_be_clickable(locator)|Espera a que el elemento sea visible y habilitado para hacer clic en el mismo|WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.NAME,“accept_button”)))
element_to_be_selected(element)|Espera a que un elemento sea seleccionado|subscription = self.driver.find_element_by_name(“terms”). WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_selected(terms)))
invisibility_of_element_located(locator)|Espera a que un elemento no sea visible o no se encuentre presente en el DOM|WebDriverWait(self.driver,10).until(expected_conditions.invisibility_of_element_located((By.ID,“loading_banner”)))
presence_of_all_elements_located(locator)|Espera a que por lo menos uno de los elementos que se indican coincida con los presentes en el sitio|WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,“input-text”)))
presence_of_element_located(locator)|Espera a que un elemento sea visible se encuentre presente en el DOM|WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.ID,“search-bar”)))
text_to_be_present_in_element(locator,text_)|Espera a que un elemento con el texto indicado se encuentre presente|WebDriverWait(self.driver,10).until(expected_conditions.text_to_be_present_in_element((By.ID,“seleorder”),“high”))
title_contains(title)|Espera a que la página contenga en el título exactamente como es indicado|WebDriverWait(self.driver, 10).until(expected_conditions.title_contains(“Welcome”))
title_is(title)|Espera a que la página tenga un título idéntico a como es indicado|WebDriverWait(self.driver, 10).until(expected_conditions.title_is(“Welcome to Platzi”))
visibility_of(element)|Espera a que el elemento indicado esté en el DOM, sea visible, su alto y ancho sean mayores a cero|first_name = self.driver.find_element_by_id(“firstname”) WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(first_name))
visibility_of_element_located(locator)|Espera a que el elemento indicado por su selector esté en el DOM, sea visible y que su alto y ancho sean mayores a cero|WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.ID,“firstname”)))

## Retos

[Sitio web de los retos](https://the-internet.herokuapp.com/)

### Agregar y eliminar elementos

Pudimos agregar y eliminar elementos con una página web de prueba, la cual es [esta](https://the-internet.herokuapp.com/add_remove_elements/)

add_remove_elements.py:

```python
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
```

### Elementos dinámicos

La página usada en esta clase es [esta](https://the-internet.herokuapp.com/disappearing_elements)

**Contexto:** En esta página hay varios botones, 1 de ellos a veces aparece y a veces no.

Creamos un script que recargará la página tantas veces como sea necesario hasta que el botón esté visible.

dynamic_elements.py:

```python
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
```

### Controles dinámicos

**IMPORTANTE**: TODAS LAS FUNCIONES DE SELENIUM DEBEN EMPEZAR CON 'test', de lo contrario, no se ejecutarán.

Esta vez usamos [esta página web](https://the-internet.herokuapp.com/dynamic_controls)

dynamic_controls.py:

```python
import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DynamicControls(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver' , options=options)
    driver = cls.driver
    driver.get('https://the-internet.herokuapp.com/dynamic_controls')


  def test_addRemoveCheckBox(self):
    driver = self.driver

    #Conseguir los elemetos
    check_box = driver.find_element_by_css_selector('#checkbox')
    add_remove_button = driver.find_element_by_css_selector('#checkbox-example > button')

    #Interactuar con los elementos
    check_box.click()
    add_remove_button.click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox')))
    add_remove_button.click()


  def test_write_in_input_field(self):
    driver = self.driver

    #Conseguir los elemetos
    enable_disable_button = driver.find_element_by_css_selector('#input-example > button')
    input_field = driver.find_element_by_css_selector('#input-example > input[type=text]')

    #Interactuar con los elementos
    enable_disable_button.click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))
    input_field.clear() #En caso de que tenga texto escrito
    input_field.send_keys('Platzi')
    enable_disable_button.click()


  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()


if __name__ == '__main__':
  unittest.main(verbosity = 2)
```

### Typos

Vamos a valiar que el texto de un sitio web sea idéntico a uno que esperamos.

typos.py:

```python
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
```

### Ordenas tablas

Usamos [esta página para esta clase](https://the-internet.herokuapp.com/tables)

Logramos conseguir la información de la primera tabla con este código:

tables.py

```python
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
```
