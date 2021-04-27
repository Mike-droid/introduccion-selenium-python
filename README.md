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
