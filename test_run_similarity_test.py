'''Tests for Part(e): running test.'''
import unittest
import synonyms as syn
import c_solution as sol
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
class TestCaseE(unittest.TestCase):

    vecs = {'this': {'is':4, 'file':3, 'one':1, 'two':1, 'three':1, 'the':1, 'third':1, 'sentence':1},
'is': {'this':4, 'file':3, 'one':1, 'two':1, 'three':1, 'the':1, 'third':1, 'sentence':1},
'file': {'this':3, 'is':3, 'one':1, 'two':2, 'has':2, 'sentences':2, 'three':2},
'one': {'this':1, 'is':1, 'file':1},
'two': {'this':1, 'is':1, 'file':2, 'has':1, 'sentences':1},
'has': {'file':2, 'two':1, 'sentences':2, 'three':1},
'sentences': {'file':2, 'two':1, 'three':1, 'has':2},
'the': {'this':1, 'is':1, 'third':1, 'sentence':1},
'third': {'this':1, 'is':1, 'the':1, 'sentence':1},
'sentence': {'this':1, 'is':1, 'the':1, 'third':1}}

    def setUp(self):
        pass

    @weight(1)
    @visibility("visible")
    def test_run_similarity_test_01(self):
        '''01: test based on cases in part d'''
        try:
            pc1 = syn.run_similarity_test('c_dummy_test1.txt', self.vecs,sol.cosine_similarity)
        except:
            pc1 = None
        try:
            pc2 = syn.run_similarity_test('c_dummy_test1_.txt', self.vecs,sol.cosine_similarity)
        except:
            pc2 = None
        expected = (pc1 == 100.0 or pc1 == 1.0 or pc2 == 100.0 or pc2 == 1.0) # allow both ways of representing percentages
        self.assertEqual(expected, True)
    @weight(1)
    @visibility("visible")
    def test_run_similarity_test_02(self):
        '''02: test based on cases in part d'''
        try:
            pc1 = syn.run_similarity_test('c_dummy_test2.txt', self.vecs,sol.cosine_similarity)
        except:
            pc1 = None
        try:
            pc2 = syn.run_similarity_test('c_dummy_test2_.txt', self.vecs,sol.cosine_similarity)
        except:
            pc2 = None
        expected = (pc1 == 0.0 or pc2 == 0.0) # allow both ways of representing percentages
        self.assertEqual(expected, True)

    @weight(1)
    @visibility("visible")
    def test_run_similarity_test_03(self):
        '''03: test based on cases in part d'''
        try:
            pc1 = syn.run_similarity_test('c_dummy_test3.txt', self.vecs,sol.cosine_similarity)
        except:
            pc1 = None
        try:
            pc2 = syn.run_similarity_test('c_dummy_test3_.txt', self.vecs,sol.cosine_similarity)
        except:
            pc2 = None
        expected = (pc1 == 0.0 or pc2 == 0.0) # allow both ways of representing percentages
        self.assertEqual(expected, True)
    @weight(1)
    @visibility("visible")
    def test_run_similarity_test_04(self):
        '''04: test based on cases in part d'''
        try:
            pc1 = syn.run_similarity_test('c_dummy_test4.txt', self.vecs,sol.cosine_similarity)
        except:
            pc1 = None
        try:
            pc2 = syn.run_similarity_test('c_dummy_test4_.txt', self.vecs,sol.cosine_similarity)
        except:
            pc2 = None
        expected = (pc1 == 100.0 or pc1 == 1.0 or pc2 == 100.0 or pc2 == 1.0) # allow both ways of representing percentages
        self.assertEqual(expected, True)

    @weight(1)
    @visibility("visible")
    def test_run_similarity_test_05(self):
        '''05: test based on cases in part d'''
        try:
            pc1 = syn.run_similarity_test('c_dummy_test5.txt', self.vecs,sol.cosine_similarity)
        except:
            pc1 = None
        try:
            pc2 = syn.run_similarity_test('c_dummy_test5_.txt', self.vecs,sol.cosine_similarity)
        except:
            pc2 = None
        expected = (pc1 == 0.0 or pc2 == 0.0) # allow both ways of representing percentages
        self.assertEqual(expected, True)

if __name__ == '__main__':
    unittest.main()

'''
Test cases
01: test based on cases in part d
'''
