'''Tests for Part(a): getting lists of sentences.'''
#from utam.tools import *
import unittest
import synonyms as syn
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
from unittest import mock
import os

class TestCaseA(unittest.TestCase):

    def setUp(self):
        self.myf = ['siavash_kazemian_temp.txt']
        
    def assertAlmostEqual(self, actual, expected):
        def dict_almost_equal(actual, expected):
            def intersect_len(d1, d2):
                return len(set(d1.keys())&set(d2.keys()))
            
            if intersect_len(expected, actual) < .7*min(len(expected), len(actual)):
                return False
                
            for k in expected:
                count = 0
                for k1 in expected[k]:
                    try:
                        if expected[k][k1] == actual[k][k1]:
                            count += 1
                    except:
                        pass
                
                if count < .7*len(expected[k]):
                    return False
                        
                    
            return True
    @weight(1)
    @visibility("hidden")        
    def test_get_sentence_lists_02(self):
        '''02: one sentence'''
        with open(self.myf[0],'w') as f:
            text = 'this is one sentence.'
            f.write(text)
        
        output = {'is': {'one': 1, 'this': 1, 'sentence': 1}, 'one': {'is': 1, 'this': 1, 'sentence': 1}, 'this': {'is': 1, 'one': 1, 'sentence': 1}, 'sentence': {'is': 1, 'one': 1, 'this': 1}}
        #assert_equal(syn.build_semantic_descriptors_from_files(self.myf),output)
        self.assertEqual(syn.build_semantic_descriptors_from_files(self.myf),output)


    @weight(1)
    @visibility("hidden") 
    def test_get_sentence_lists_02_almost(self):
        '''02: one sentence'''
        with open(self.myf[0],'w') as f:
            text = 'this is one sentence.'
            f.write(text)
        
        output = {'is': {'one': 1, 'this': 1, 'sentence': 1}, 'one': {'is': 1, 'this': 1, 'sentence': 1}, 'this': {'is': 1, 'one': 1, 'sentence': 1}, 'sentence': {'is': 1, 'one': 1, 'this': 1}}
        #assert_equal(syn.build_semantic_descriptors_from_files(self.myf),output)
        self.assertAlmostEqual(syn.build_semantic_descriptors_from_files(self.myf),output)



    @weight(1)
    @visibility("hidden")
    def test_get_sentence_lists_03(self):
        '''03: multiple sentences'''
        with open(self.myf[0],'w') as f:
            text = 'this is one sentence. here is another sentence.'
            f.write(text)
    
        output = {'here': {'is': 1, 'another': 1, 'sentence': 1}, 'this': {'is': 1, 'one': 1, 'sentence': 1}, 'sentence': {'is': 2, 'another': 1, 'here': 1, 'one': 1, 'this': 1}, 'is': {'another': 1, 'here': 1, 'one': 1, 'this': 1, 'sentence': 2}, 'one': {'is': 1, 'this': 1, 'sentence': 1}, 'another': {'is': 1, 'here': 1, 'sentence': 1}}
        #assert_equal(syn.build_semantic_descriptors_from_files(self.myf),output)
        self.assertEqual(syn.build_semantic_descriptors_from_files(self.myf),output)
    
    
    @weight(1)
    @visibility("hidden")
    def test_get_sentence_lists_03_almost(self):
        '''03: multiple sentences'''
        with open(self.myf[0],'w') as f:
            text = 'this is one sentence. here is another sentence.'
            f.write(text)
    
        output = {'here': {'is': 1, 'another': 1, 'sentence': 1}, 'this': {'is': 1, 'one': 1, 'sentence': 1}, 'sentence': {'is': 2, 'another': 1, 'here': 1, 'one': 1, 'this': 1}, 'is': {'another': 1, 'here': 1, 'one': 1, 'this': 1, 'sentence': 2}, 'one': {'is': 1, 'this': 1, 'sentence': 1}, 'another': {'is': 1, 'here': 1, 'sentence': 1}}
        #assert_equal(syn.build_semantic_descriptors_from_files(self.myf),output)
        self.assertAlmostEqual(syn.build_semantic_descriptors_from_files(self.myf),output)
    
    
    @weight(1)
    @visibility("hidden")
    def test_get_sentence_lists_04(self):
        '''04: separation by ., ?, !'''
        with open(self.myf[0],'w') as f:
            text = 'what is going on? i did not expect that! tell me what to do.'
            f.write(text)
        
        output = {'did': {'i': 1, 'expect': 1, 'not': 1, 'that': 1}, 'tell': {'to': 1, 'what': 1, 'do': 1, 'me': 1}, 'do': {'what': 1, 'tell': 1, 'to': 1, 'me': 1}, 'what': {'on': 1, 'to': 1, 'tell': 1, 'do': 1, 'is': 1, 'going': 1, 'me': 1}, 'going': {'is': 1, 'on': 1, 'what': 1}, 'expect': {'did': 1, 'i': 1, 'not': 1, 'that': 1}, 'not': {'did': 1, 'i': 1, 'expect': 1, 'that': 1}, 'on': {'is': 1, 'going': 1, 'what': 1}, 'to': {'what': 1, 'tell': 1, 'do': 1, 'me': 1}, 'that': {'did': 1, 'i': 1, 'expect': 1, 'not': 1}, 'is': {'on': 1, 'what': 1, 'going': 1}, 'i': {'did': 1, 'not': 1, 'expect': 1, 'that': 1}, 'me': {'what': 1, 'tell': 1, 'do': 1, 'to': 1}}
        #assert_equal(syn.build_semantic_descriptors_from_files(self.myf),output)
        self.assertEqual(syn.build_semantic_descriptors_from_files(self.myf),output)
    
    

    @weight(1)
    @visibility("hidden")
    def test_get_sentence_lists_04_almost(self):
        '''04: separation by ., ?, !'''
        with open(self.myf[0],'w') as f:
            text = 'what is going on? i did not expect that! tell me what to do.'
            f.write(text)
        
        output = {'did': {'i': 1, 'expect': 1, 'not': 1, 'that': 1}, 'tell': {'to': 1, 'what': 1, 'do': 1, 'me': 1}, 'do': {'what': 1, 'tell': 1, 'to': 1, 'me': 1}, 'what': {'on': 1, 'to': 1, 'tell': 1, 'do': 1, 'is': 1, 'going': 1, 'me': 1}, 'going': {'is': 1, 'on': 1, 'what': 1}, 'expect': {'did': 1, 'i': 1, 'not': 1, 'that': 1}, 'not': {'did': 1, 'i': 1, 'expect': 1, 'that': 1}, 'on': {'is': 1, 'going': 1, 'what': 1}, 'to': {'what': 1, 'tell': 1, 'do': 1, 'me': 1}, 'that': {'did': 1, 'i': 1, 'expect': 1, 'not': 1}, 'is': {'on': 1, 'what': 1, 'going': 1}, 'i': {'did': 1, 'not': 1, 'expect': 1, 'that': 1}, 'me': {'what': 1, 'tell': 1, 'do': 1, 'to': 1}}
        #assert_equal(syn.build_semantic_descriptors_from_files(self.myf),output)
        self.assertAlmostEqual(syn.build_semantic_descriptors_from_files(self.myf),output)
    
    
    @weight(1)
    @visibility("hidden")
    def test_get_sentence_lists_05(self):
        '''05: ?!'''
        with open(self.myf[0],'w') as f:
            text = 'who goes there?!'
            f.write(text)
        
        output = {'who': {'there': 1, 'goes': 1}, 'there': {'who': 1, 'goes': 1}, 'goes': {'who': 1, 'there': 1}}
        #assert_equal(syn.build_semantic_descriptors_from_files(self.myf),output)
        self.assertEqual(syn.build_semantic_descriptors_from_files(self.myf),output)
    
    
    @weight(1)
    @visibility("hidden")
    def test_get_sentence_lists_05_almost(self):
        '''05: ?!'''
        with open(self.myf[0],'w') as f:
            text = 'who goes there?!'
            f.write(text)
        
        output = {'who': {'there': 1, 'goes': 1}, 'there': {'who': 1, 'goes': 1}, 'goes': {'who': 1, 'there': 1}}
        #assert_equal(syn.build_semantic_descriptors_from_files(self.myf),output)
        self.assertAlmostEqual(syn.build_semantic_descriptors_from_files(self.myf),output)
    
    
    
    @weight(1)
    @visibility("hidden")
    def test_get_sentence_lists_07(self):
        '''07: word separation by punctuation'''
        with open(self.myf[0],'w') as f:
            text = 'I, Robot: the best novel by Asimov; the worst; or neither?'
            f.write(text)
        
        output = {'robot': {'novel': 1, 'by': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'i': 1, 'the': 1, 'or': 1}, 'novel': {'robot': 1, 'by': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'i': 1, 'the': 1, 'or': 1}, 'by': {'robot': 1, 'novel': 1, 'i': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'the': 1, 'or': 1}, 'best': {'novel': 1, 'by': 1, 'robot': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'i': 1, 'the': 1, 'or': 1}, 'asimov': {'robot': 1, 'novel': 1, 'by': 1, 'best': 1, 'or': 1, 'worst': 1, 'neither': 1, 'i': 1, 'the': 1}, 'worst': {'robot': 1, 'novel': 1, 'by': 1, 'best': 1, 'asimov': 1, 'neither': 1, 'i': 1, 'the': 1, 'or': 1}, 'neither': {'robot': 1, 'novel': 1, 'i': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'by': 1, 'the': 1, 'or': 1}, 'i': {'robot': 1, 'novel': 1, 'by': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'the': 1, 'or': 1}, 'the': {'novel': 1, 'by': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'i': 1, 'robot': 1, 'or': 1}, 'or': {'robot': 1, 'novel': 1, 'by': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'i': 1, 'the': 1}}
        #assert_equal(syn.build_semantic_descriptors_from_files(self.myf),output)
        self.assertEqual(syn.build_semantic_descriptors_from_files(self.myf),output)
        
    @weight(1)
    @visibility("hidden")
    def test_get_sentence_lists_07_almost(self):
        '''07: word separation by punctuation'''
        with open(self.myf[0],'w') as f:
            text = 'I, Robot: the best novel by Asimov; the worst; or neither?'
            f.write(text)
        
        output = {'robot': {'novel': 1, 'by': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'i': 1, 'the': 1, 'or': 1}, 'novel': {'robot': 1, 'by': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'i': 1, 'the': 1, 'or': 1}, 'by': {'robot': 1, 'novel': 1, 'i': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'the': 1, 'or': 1}, 'best': {'novel': 1, 'by': 1, 'robot': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'i': 1, 'the': 1, 'or': 1}, 'asimov': {'robot': 1, 'novel': 1, 'by': 1, 'best': 1, 'or': 1, 'worst': 1, 'neither': 1, 'i': 1, 'the': 1}, 'worst': {'robot': 1, 'novel': 1, 'by': 1, 'best': 1, 'asimov': 1, 'neither': 1, 'i': 1, 'the': 1, 'or': 1}, 'neither': {'robot': 1, 'novel': 1, 'i': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'by': 1, 'the': 1, 'or': 1}, 'i': {'robot': 1, 'novel': 1, 'by': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'the': 1, 'or': 1}, 'the': {'novel': 1, 'by': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'i': 1, 'robot': 1, 'or': 1}, 'or': {'robot': 1, 'novel': 1, 'by': 1, 'best': 1, 'asimov': 1, 'worst': 1, 'neither': 1, 'i': 1, 'the': 1}}
        #assert_equal(syn.build_semantic_descriptors_from_files(self.myf),output)
        self.assertAlmostEqual(syn.build_semantic_descriptors_from_files(self.myf),output)
    
    
    @weight(1)
    @visibility("hidden")
    def test_get_sentence_lists_11(self):
        '''11: ignores irrelevant spaces'''
        with open(self.myf[0],'w') as f:
            text = '  my goodness   your width   has   grown   .'
            f.write(text)
        
        output = {'width': {'goodness': 1, 'has': 1, 'my': 1, 'grown': 1, 'your': 1}, 'goodness': {'width': 1, 'has': 1, 'my': 1, 'grown': 1, 'your': 1}, 'your': {'width': 1, 'has': 1, 'my': 1, 'grown': 1, 'goodness': 1}, 'has': {'width': 1, 'your': 1, 'my': 1, 'grown': 1, 'goodness': 1}, 'my': {'width': 1, 'has': 1, 'goodness': 1, 'grown': 1, 'your': 1}, 'grown': {'width': 1, 'has': 1, 'my': 1, 'goodness': 1, 'your': 1}}

        self.assertEqual(syn.build_semantic_descriptors_from_files(self.myf),output)

if __name__ == '__main__':
    unittest.main()

'''
Test cases:
01: empty string
02: one sentence
03: multiple sentences
04: separation by ., ?, !
05: word separation
DELETED 06: sentence with 1 word
07: word separation by punctuation
DELETED 09: word separation by newline
DELETED 10: ignores irrelevant punctuation
11: ignores irrelevant space
'''
