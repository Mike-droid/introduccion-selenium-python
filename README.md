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
