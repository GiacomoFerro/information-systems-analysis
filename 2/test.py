import unittest
from Irpef import irpef_calculation

class test_CalcoloIrpef(unittest.TestCase):

    def test_calcola_irpef(self):
        #print(irpef_calculation(24000.0))
        self.assertEqual(3720.0, irpef_calculation(16000))
        self.assertEqual(115.0, irpef_calculation(500))
        self.assertEqual(13040.0, irpef_calculation(44000.0))
        self.assertEqual(19270.0,irpef_calculation(60000))
        self.assertEqual(31870.0, irpef_calculation(90000.0))


#if __name__ == '__main__':
#	unittest.main()


# Avvio manuale di tutti i test mediante suite
#creo la suite
#faccio lartire la suite con i vari test
suite = unittest.TestLoader().loadTestsFromTestCase(test_CalcoloIrpef)
unittest.TextTestRunner(verbosity=2).run(suite)

# Composizione manuale di una suite di test
#aggiungo i test alla suite
suite = unittest.TestSuite()
suite.addTest(test_CalcoloIrpef('test_calcola_irpef'))

unittest.TextTestRunner(verbosity=2).run(suite)
