

import math
from operator import sub

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 2.
    '''
    
    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)

def cheb_sim(vec1,vec2):
    all_keys = set(vec1.keys()) | set(vec2.keys())
    the_max = 0
    for k in all_keys:
        diff  = abs(vec1.get(k,0) - vec2.get(k,0))
        the_max = max(the_max,diff)
    return math.exp(-1*the_max)

def cosine_similarity(vec1, vec2):
    '''Return the cosine similarity of sparse vectors vec1 and vec2,
    stored as dictionaries as described in the handout for Project 2.
    '''
    
    dot_product = 0.0  # floating point to handle large numbers
    for x in vec1:
        if x in vec2:
            dot_product += vec1[x] * vec2[x]
    
    # Make sure empty vectors don't cause an error -- return -1 as
    # suggested in the handout for Project 2.
    norm_product = norm(vec1) * norm(vec2)
    if norm_product == 0.0:
        return -1.0
    else:
        return dot_product / norm_product


