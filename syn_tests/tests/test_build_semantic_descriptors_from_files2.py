'''Tests for Part(b): Extracting sentences from files.'''
import unittest
import synonyms as syn
from gradescope_utils.autograder_utils.decorators import weight, visibility, number

class TestBuildSemanticDescriptorsFromFiles2(unittest.TestCase):

    def setUp(self):
        pass

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
            
        self.assertEqual(dict_almost_equal(actual, expected), True)

    @weight(1)
    @visibility("hidden")
    def test_get_sentence_lists_from_files_02(self):
        '''02: one files'''
        files = ['c_file1.txt']
        
        expected = {'is': {'file': 1, 'one': 1, 'this': 1}, 'file': {'is': 1, 'one': 1, 'this': 1}, 'one': {'is': 1, 'file': 1, 'this': 1}, 'this': {'is': 1, 'file': 1, 'one': 1}}
        #assert_equal(syn.get_sentence_lists_from_files(files),output)
        self.assertEqual(syn.build_semantic_descriptors_from_files(files),expected)
        
    @weight(1)
    @visibility("hidden")
    def test_get_sentence_lists_from_files_02_almost(self):
        '''02: one files'''
        files = ['c_file1.txt']
        
        expected = {'is': {'file': 1, 'one': 1, 'this': 1}, 'file': {'is': 1, 'one': 1, 'this': 1}, 'one': {'is': 1, 'file': 1, 'this': 1}, 'this': {'is': 1, 'file': 1, 'one': 1}}
        #assert_equal(syn.get_sentence_lists_from_files(files),output)
        self.assertAlmostEqual(syn.build_semantic_descriptors_from_files(files),expected)


    @weight(1)
    @visibility("hidden")
    def test_get_sentence_lists_from_files_03(self):
        '''03: multiple files'''
        files = ['c_file1.txt', 'c_file2.txt', 'c_file3.txt']
        
        expected = {'three': {'sentences': 2, 'this': 1, 'is': 1, 'has': 2, 'file': 3, 'two': 1, 'four': 1}, 'two': {'this': 1, 'three': 1, 'is': 1, 'has': 1, 'file': 2, 'sentences': 1}, 'the': {'is': 1, 'this': 1, 'sentence': 1, 'third': 1}, 'third': {'is': 1, 'this': 1, 'sentence': 1, 'the': 1}, 'this': {'sentence': 1, 'is': 4, 'three': 1, 'file': 3, 'one': 1, 'two': 1, 'the': 1, 'third': 1}, 'four': {'three': 1, 'file': 1, 'sentences': 1, 'has': 1}, 'has': {'three': 2, 'file': 2, 'sentences': 2, 'two': 1, 'four': 1}, 'is': {'this': 4, 'sentence': 1, 'three': 1, 'file': 3, 'one': 1, 'two': 1, 'the': 1, 'third': 1}, 'sentences': {'has': 2, 'file': 2, 'two': 1, 'four': 1, 'three': 2}, 'file': {'this': 3, 'four': 1, 'three': 3, 'is': 3, 'has': 2, 'two': 2, 'one': 1, 'sentences': 2}, 'one': {'is': 1, 'file': 1, 'this': 1}, 'sentence': {'is': 1, 'this': 1, 'the': 1, 'third': 1}}
        self.assertEqual(syn.build_semantic_descriptors_from_files(files),expected)

    

if __name__ == '__main__':
    unittest.main()

'''
Test cases:
02: one file
03: multiple files
'''
