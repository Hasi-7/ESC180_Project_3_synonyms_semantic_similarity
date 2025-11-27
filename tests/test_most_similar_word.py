'''Tests for Part(d): returning most similar word.'''
import unittest
import synonyms as syn
import c_solution as sol
from gradescope_utils.autograder_utils.decorators import weight, visibility, number

class TestCaseD(unittest.TestCase):

    def setUp(self):
        pass
    @weight(1)
    @visibility("visible")
    def test_most_similar_word_01(self):
        '''01: most similar word is itself'''
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
        word = 'this'
        choices = ['is','file','this']
        output = syn.most_similar_word(word, choices, vecs,sol.cosine_similarity)
        #assert_equal(output,'this')
        self.assertEqual(output,'this')
    @weight(1)
    @visibility("visible")   
    def test_most_similar_word_02(self):
        '''02: test from data'''
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
        word = 'third'
        choices = ['is','one','two']
        output = syn.most_similar_word(word, choices, vecs,sol.cosine_similarity)
        #assert_equal(output,'1')
        self.assertEqual(output,'one')
    
    @weight(1)
    @visibility("visible")
    def test_most_similar_word_03(self):
        '''03: test from data--tie return smallest element'''
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
        vecs['four'] = {'this':1, 'is':1, 'file':1} # identical to 1
        word = 'this'
        choices = ['one','four']
        output = syn.most_similar_word(word, choices, vecs,sol.cosine_similarity)
        #assert_equal(output,'1')
        self.assertEqual(output,'one')
        choices = ['four','one']
        output = syn.most_similar_word(word, choices, vecs,sol.cosine_similarity)
        #assert_equal(output,'4')
        self.assertEqual(output,'four')
 
    @weight(1)
    @visibility("visible")   
    def test_most_similar_word_04(self):
        '''04: unknown word in choices'''
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
        word = 'third'
        choices = ['four','one','two']
        output = syn.most_similar_word(word, choices, vecs,sol.cosine_similarity)
        #assert_equal(output,'1')
        self.assertEqual(output,'one')
   
 
    @weight(1)
    @visibility("visible")
    def test_most_similar_word_06(self):
        '''04: unknown word in choices'''
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
        word = 'third'
        choices = ['four','siavash','kaldi']
        output = syn.most_similar_word(word, choices, vecs,sol.cosine_similarity)
        #assert_equal(output,'1')
        self.assertEqual(output,'four')

    @weight(1)
    @visibility("visible")
    def test_most_similar_word_05(self):
        '''05: unknown word queried'''
        vecs = {'this': {'is':4, 'file':3, 'one':1, 'two':1, 'three':1, 'the':1, 'third':1, 'sentence':1},
'is': {'this':4, 'file':3, 'one':1, 'two':1, 'three':1, 'the':1, 'third':1, 'sentence':1},
'file': {'this':3, 'is':3, 'one':1, 'two':2, 'has':2, 'sentences':2, 'three':2},
'one': {'this':1, 'is':1, 'file':1},
'two': {'this':1, 'is':1, 'file':2, 'has':1, 'sentences':1},
'has': {'file':2, 'two':1, 'sentences':2, 'three':1},
'sentences': {'file':2, 'one':1, 'three':1, 'has':2},
'the': {'this':1, 'is':1, 'third':1, 'sentence':1},
'third': {'this':1, 'is':1, 'the':1, 'sentence':1},
'sentence': {'this':1, 'is':1, 'the':1, 'third':1}}
        word = 'blah'
        choices = ['not','in','corpus']
        output = syn.most_similar_word(word, choices, vecs,sol.cosine_similarity)
        #assert_equal(output,'not')
        self.assertEqual(output,'not')

    @weight(1)
    @visibility("visible")
    def test_diff_sim_func(self):
        vecs = {'a1':{'a2':1,'a3':2},'a4':{'a2':2,'a3':1},'a5':{'a2':4,'a3':4}}
        choices = ['blah','a4','a5']
        word = 'a1'
        output = syn.most_similar_word(word, choices, vecs,sol.cheb_sim)
        #assert_equal(output,'not')
        self.assertEqual(output,'a4')

if __name__ == '__main__':
    unittest.main()
    
'''
Test cases
01: most similar word is itself
02: test from data
03: test from data--tie return smallest element
04: unknown word in choices
05: unknown word queried
06: all choices unknown
07: works with cheb sim function 4,4, is further from 2,1 than is 1,2
'''
