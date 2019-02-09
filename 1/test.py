import unittest
from CodiceFiscale import estrai_nome, estrai_cognome, genera_mese, codice_comune, genera_giorno, genera_codice_controllo

class test_codiceFiscale(unittest.TestCase):
    def test_estrai_nome(self):
        self.assertEqual("gpn", estrai_nome("gino pino"))
        self.assertEqual("tzn", estrai_nome("tiziana"))
        self.assertEqual("lcu", estrai_nome("luca"))
        self.assertEqual("cex", estrai_nome("ce"))

    def test_estrai_cognome(self):
        self.assertEqual("rso", estrai_cognome("rosi"))
        self.assertEqual("fox", estrai_cognome("fo"))
        self.assertEqual("dls", estrai_cognome("d'alessandro"))
        self.assertEqual("dli", estrai_cognome("di leo"))

    def test_genera_mese(self):
        self.assertEqual("d", genera_mese("4"))

    def test_codice_comune(self):
        self.assertEqual("e512", codice_comune("legnago"))
        self.assertEqual("f861", codice_comune("negrar"))

    def test_genera_giorno(self):
        self.assertEqual("16", genera_giorno("16", "m"))
        self.assertEqual("52", genera_giorno("12", "f"))

    def test_genera_codice_controllo(self):
        self.assertEqual("w", genera_codice_controllo("gbbfnc96h16e512"))
        self.assertEqual("n", genera_codice_controllo("frrgcm95e26f861"))
        self.assertEqual("e", genera_codice_controllo("dliddg96r16f861"))
        self.assertEqual("x", genera_codice_controllo("rssrse96s03l781"))
        self.assertEqual("a", genera_codice_controllo("tffnna96b54a703"))

#if __name__ == '__main__':
#	unittest.main()


# Avvio manuale di tutti i test mediante suite
#creo la suite
#faccio lartire la suite con i vari test
suite = unittest.TestLoader().loadTestsFromTestCase(test_codiceFiscale)
unittest.TextTestRunner(verbosity=2).run(suite)

# Composizione manuale di una suite di test
#aggiungo i test alla suite
suite = unittest.TestSuite()
suite.addTest(test_codiceFiscale('test_estrai_nome'))
suite.addTest(test_codiceFiscale('test_estrai_cognome'))
suite.addTest(test_codiceFiscale('test_genera_mese'))
suite.addTest(test_codiceFiscale('test_codice_comune'))
suite.addTest(test_codiceFiscale('test_genera_giorno'))
suite.addTest(test_codiceFiscale('test_genera_codice_controllo'))
unittest.TextTestRunner(verbosity=2).run(suite)
