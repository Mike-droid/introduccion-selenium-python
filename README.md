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
