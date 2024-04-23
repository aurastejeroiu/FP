from repository.clientiRepo import clientiRepo
from repository.filmeRepo import filmeRepo
from repository.inchirieriRepo import inchirieriRepo

import unittest
from domain.client import TestCaseClient
from domain.film import TestCaseFilm
from domain.inchiriere import TestCaseInchiriere
from domain.validatoare import TestCaseValidatoare
from repository.clientiRepo import TestCaseClientiRepo
from repository.filmeRepo import TestCaseFilmeRepo
from repository.inchirieriRepo import TestCaseInchirieriRepo
from service.clientiServ import TestCaseClientiServ
from service.inchirieriServ import TestCaseInchirieriServ

def runTests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((
        loader.loadTestsFromTestCase(TestCaseClient),
        loader.loadTestsFromTestCase(TestCaseFilm),
        loader.loadTestsFromTestCase(TestCaseInchiriere),
        loader.loadTestsFromTestCase(TestCaseValidatoare),
        loader.loadTestsFromTestCase(TestCaseClientiRepo),
        loader.loadTestsFromTestCase(TestCaseFilmeRepo),
        loader.loadTestsFromTestCase(TestCaseInchirieriRepo),
        loader.loadTestsFromTestCase(TestCaseClientiServ),
        loader.loadTestsFromTestCase(TestCaseInchirieriServ),
        ))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)

runTests()

print('\n')

from ui.console import console

clienti = clientiRepo()
filme = filmeRepo()
inchirieri = inchirieriRepo()


ui = console(clienti, filme, inchirieri)
ui.showUI()