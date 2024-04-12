from Lab5 import Gramamr
import unittest

class TestGrammar(unittest.TestCase):
    def setUp(self):
        self.g = Gramamr()
        self.P1, self.P2, self.P3, self.P4, self.P5 = self.g.ReturnProductions() 

    def test_remove_epsilon(self):
        # Test RemoveEpsilon method
        expected_result = {'S': ['dB', 'd', 'dS', 'aAdAB'], 'A': ['d', 'dS', 'aAdAB'], 'B': ['aS', 'a', 'd', 'dS', 'aAdAB'], 'E': ['AS']}
        self.assertEqual(self.P1, expected_result)
    
    def test_eliminate_unit_prod(self):
        # Test EliminateUnitProd method
        expected_result = {'S': ['dB', 'd', 'dS', 'aAdAB'], 'A': ['d', 'dS', 'aAdAB'], 'B': ['aS', 'a', 'd', 'dS', 'aAdAB'], 'E': ['AS']}
        self.assertEqual(self.P2, expected_result)

    def test_eliminate_inaccesible(self):
        # Test EliminateInaccesible method
        expected_result = {'S': ['dB', 'd', 'dS', 'aAdAB'], 'A': ['d', 'dS', 'aAdAB'], 'B': ['aS', 'a', 'd', 'dS', 'aAdAB']}
        self.assertEqual(self.P3, expected_result)

    def test_remove_unprod(self):
        # Test RemoveUnprod method
        expected_result = {'S': ['dB', 'd', 'dS', 'aAdAB'], 'A': ['d', 'dS', 'aAdAB'], 'B': ['aS', 'a', 'd', 'dS', 'aAdAB']}
        self.assertEqual(self.P4, expected_result)

    def test_obtain_cnf(self):
        # Test ObtainCNF method
        expected_result = {'S': ['CD', 'd', 'CE', 'FG'], 'A': ['d', 'CE', 'FG'], 'B': ['HE', 'a', 'd', 'CE', 'FG'], 'C': ['d'], 'D': ['B'], 'E': ['S'], 'F': ['aA'], 'G': ['dAB'], 'H': ['a']}
        self.assertEqual(self.P5, expected_result)

if __name__ == '__main__':
    unittest.main()