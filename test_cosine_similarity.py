'''Tests for Part(c): Buildling coocurrence vectors.'''
import unittest
import synonyms as syn
from gradescope_utils.autograder_utils.decorators import weight, visibility, number

from unittest import mock

def norm(vec):
    import math
    
    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)
def cosine_similarity(vec1, vec2):
    
    dot_product = 0.0  
    for x in vec1:
        if x in vec2:
            dot_product += vec1[x] * vec2[x]
    
    norm_product = norm(vec1) * norm(vec2)
    if norm_product == 0.0:
        return -1.0
    else:
        return dot_product / norm_product


class TestBuildSemanticDescriptors(unittest.TestCase):

    def setUp(self):
        self.vec1 = {'this':1, 'is':1, 'the':1, 'sentence':1}
        self.vec2 = {'this':2, 'is':1, 'the':2, 'sentence':1}
        self.vec3 = {'this':1, 'is':1, 'there':1, 'sentences':1}
        self.vec4 = {'my':1, 'lord':1, 'please':1, 'forgive':1}

    @weight(1)
    @visibility("visible")
    def test_cos_sim_01(self):
        expected = cosine_similarity(self.vec1,self.vec1)
        hyp = syn.cosine_similarity(self.vec1,self.vec1)
        self.assertAlmostEqual(hyp,expected, places=3)

    @weight(1)
    @visibility("visible")
    def test_cos_sim_02(self):
        expected = cosine_similarity(self.vec1,self.vec2)
        hyp = syn.cosine_similarity(self.vec1,self.vec2)
        self.assertAlmostEqual(hyp,expected, places=3)

    @weight(1)
    @visibility("visible")
    def test_cos_sim_03(self):
        expected = cosine_similarity(self.vec1,self.vec3)
        hyp = syn.cosine_similarity(self.vec1,self.vec3)
        self.assertAlmostEqual(hyp,expected, places=3)

    @weight(1)
    @visibility("visible")
    def test_cos_sim_04(self):
        expected = cosine_similarity(self.vec1,self.vec4)
        hyp = syn.cosine_similarity(self.vec1,self.vec4)
        self.assertAlmostEqual(hyp,expected, places=3)


if __name__ == '__main__':
    unittest.main()
