'''Tests for Part(c): Buildling coocurrence vectors.'''
import unittest
import synonyms as syn
from gradescope_utils.autograder_utils.decorators import weight, visibility, number

class TestBuildSemanticDescriptors(unittest.TestCase):

    def setUp(self):
        pass

    @weight(1)
    @visibility("visible")
    def test_build_semantic_descriptors_01(self):
        '''01: hapax legomenon--"third"'''
        slist = [['this', 'is', 'file', 'one'],
                    ['this', 'is', 'file', 'two'],
                    ['file', 'two', 'has', 'two', 'sentences'],
                    ['this', 'is', 'file', 'three'],
                    ['file', 'three', 'has', 'three', 'sentences'],
                    ['this', 'is', 'the', 'third', 'sentence']]
        vecs = syn.build_semantic_descriptors(slist)
        expected = {'this':1, 'is':1, 'the':1, 'sentence':1}
        #assert_equal(vecs['third'],expected)
        self.assertEqual(vecs['third'],expected)

    @weight(1)
    @visibility("visible")
    def test_build_semantic_descriptors_02(self):
        '''02: normal word--"this"'''
        slist = [['this', 'is', 'file', 'one'],
                    ['this', 'is', 'file', 'two'],
                    ['file', 'two', 'has', 'two', 'sentences'],
                    ['this', 'is', 'file', 'three'],
                    ['file', 'three', 'has', 'three', 'sentences'],
                    ['this', 'is', 'the', 'third', 'sentence']]
        vecs = syn.build_semantic_descriptors(slist)
        expected = {'is':4, 'file':3, 'one':1, 'two':1, 'three':1, 'the':1, 'third':1, 'sentence':1}
        #assert_equal(vecs['this'],expected)
        self.assertEqual(vecs['this'],expected)

    @weight(1)
    @visibility("visible")
    def test_build_semantic_descriptors_03(self):
        '''03: normal word 2--"file"'''
        slist = [['this', 'is', 'file', 'one'],
                    ['this', 'is', 'file', 'two'],
                    ['file', 'two', 'has', 'two', 'sentences'],
                    ['this', 'is', 'file', 'three'],
                    ['file', 'three', 'has', 'three', 'sentences'],
                    ['this', 'is', 'the', 'third', 'sentence']]
        vecs = syn.build_semantic_descriptors(slist)
        expected = {'this':3, 'is':3, 'one':1, 'two':2, 'has':2, 'sentences':2, 'three':2}
        #assert_equal(vecs['file'],expected)
        self.assertEqual(vecs['file'],expected)

#    def test_build_semantic_descriptors_04(self):
#        '''04: word that occurs more than once in a sentence--"2"'''
#        slist = [['this', 'is', 'file', 'one'],
#                    ['this', 'is', 'file', 'two'],
#                    ['file', 'two', 'has', 'two', 'sentences'],
#                    ['this', 'is', 'file', 'three'],
#                    ['file', 'three', 'has', 'three', 'sentences'],
#                    ['this', 'is', 'the', 'third', 'sentence']]
#        vecs = syn.build_semantic_descriptors(slist)
#        expected = {'this':1, 'is':1, 'file':2, 'has':1, 'sentences':1}
#        #assert_equal(vecs['2'],expected)
#        self.assertEqual(vecs['two'],expected)

    @weight(1)
    @visibility("visible")
    def test_build_semantic_descriptors_06(self):
        '''06: empty input'''
        slist = [[]]
        vecs = syn.build_semantic_descriptors(slist)
        expected = {}
        #assert_equal(vecs['2'],expected)
        self.assertEqual(vecs,expected)

#   def test_build_semantic_descriptors_05(self):
#       '''05: overall'''
#       slist = [['this', 'is', 'file', 'one'],
#                   ['this', 'is', 'file', 'two'],
#                   ['file', 'two', 'has', 'two', 'sentences'],
#                   ['this', 'is', 'file', 'three'],
#                   ['file', 'three', 'has', 'three', 'sentences'],
#                   ['this', 'is', 'the', 'third', 'sentence']]
#       vecs = syn.build_semantic_descriptors(slist)
#       expected = {'this': {'is':4, 'file':3, 'one':1, 'two':1, 'three':1, 'the':1, 'third':1, 'sentence':1},
#'is': {'this':4, 'file':3, 'one':1, 'two':1, 'three':1, 'the':1, 'third':1, 'sentence':1},
#'file': {'this':3, 'is':3, 'one':1, 'two':2, 'has':2, 'sentences':2, 'three':2},
#'one': {'this':1, 'is':1, 'file':1},
#'two': {'this':1, 'is':1, 'file':2, 'has':1, 'sentences':1},
#'three': {'this':1, 'is':1, 'file':2, 'has':1, 'sentences':1},
#'has': {'file':2, 'two':1, 'sentences':2, 'three':1},
#'sentences': {'file':2, 'two':1, 'three':1, 'has':2},
#'the': {'this':1, 'is':1, 'third':1, 'sentence':1},
#'third': {'this':1, 'is':1, 'the':1, 'sentence':1},
#'sentence': {'this':1, 'is':1, 'the':1, 'third':1}}
#        #assert_equal(vecs,expected)
#        self.assertEqual(vecs,expected)

if __name__ == '__main__':
    unittest.main()

'''
load files 1, 2, and 3.
Test cases
01: hapax legomenon
02: normal word
03: normal word 2
04: word that occurs more than once in a sentence
05: overall
06: empty input
'''
