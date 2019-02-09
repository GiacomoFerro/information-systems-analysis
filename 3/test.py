import unittest
from CalcoloPasqua import pasqua
# coding=utf-8


class test_CalcoloPasqua(unittest.TestCase):

    def test_Pasqua(self):
        self.assertEqual((31.0,3,2002.0), pasqua(2002))
        self.assertEqual((15.0,4,2001.0), pasqua(2001))
        self.assertEqual((1.0,4,2018.0), pasqua(2018))
        self.assertEqual((27.0,3,2016.0), pasqua(2016))
        self.assertEqual((2.0,4,1961.0), pasqua(1961))
        self.assertEqual((3.0,4,1983.0), pasqua(1983))

#if __name__ == '__main__':
#	unittest.main()

# Avvio manuale di tutti i test mediante suite
#creo la suite
#faccio lartire la suite con i vari test
suite = unittest.TestLoader().loadTestsFromTestCase(test_CalcoloPasqua)
unittest.TextTestRunner(verbosity=2).run(suite)

# Composizione manuale di una suite di test
#aggiungo i test alla suite
suite = unittest.TestSuite()
suite.addTest(test_CalcoloPasqua('test_Pasqua'))

unittest.TextTestRunner(verbosity=2).run(suite)
