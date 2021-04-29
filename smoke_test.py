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