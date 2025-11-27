'''Semantic Similarity

Authors: Samantha Change and Muhammad Hasnain Heryani
'''

import math

def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


# Assume full vec is sorted alphabetically

def convert_sparse_to_full(vec, full_vec):
    result = []  # Must be a list
    for word in full_vec:
        result.append(vec.get(word, 0))
    return result

    # def insertion_sort(vec):
    #     for i in range(1, len(vec)):
    #         key = string_to_ascii(vec[i])
    #         j = i - 1
    #         while j >= 0 and key < string_to_ascii(vec[j]):
    #             vec[j+1] = vec[j]
    #             j -= 1
    #         vec[j+1] = key

# def string_to_ascii(word):
#     ascii_value = 0
#     for char in word:
#         ascii_value += ord(char)
#     return ascii_value

def cosine_similarity(vec1, vec2):
    full_vec = sorted(set(list(vec1.keys()) + list(vec2.keys())))

    full_vec1 = convert_sparse_to_full(vec1, full_vec)
    full_vec2 = convert_sparse_to_full(vec2, full_vec)
    dot_product = 0.0
    for i in range(len(full_vec1)):
        dot_product += full_vec1[i]*full_vec2[i]
    if (norm(vec1) * norm(vec2)) == 0:
        return -1
    return dot_product / ((norm(vec1) * norm(vec2)))

def build_semantic_descriptors(sentences):
    unique_words = {}
    for sentence in sentences:
        for word in sentence:
            if word not in unique_words.keys():
                unique_words[word] = {}
        for word in set(sentence):
            word_counts = sentence_word_counts(sentence, word)
            for key, value in word_counts.items():
                unique_words[word][key] = unique_words[word].get(key, 0) + value
    return unique_words

def sentence_word_counts(sentence, target_word):
    word_counts = {}
    for word in sentence:
        if word != target_word:
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def build_semantic_descriptors_from_files(filenames):
    all_sentences = []
    SENTENCE_SEPARATORS = [".", "!", "?"]
    SENTENCE_PUNCTUATION = [",", "-", "--", ";", ":"]
    for filename in filenames:
        with open(filename, "r", encoding = "latin1") as f:
            sentences = f.read().lower()
        for separators in SENTENCE_SEPARATORS:
            sentences = sentences.replace(separators, "%20")
        sentences = sentences.split("%20")
        for i in range(len(sentences)):
            for punctuation in SENTENCE_PUNCTUATION:
                sentences[i] = sentences[i].replace(punctuation, " ")
            sentences[i] = sentences[i].split()
        for sentence in sentences:
            if sentence:
                all_sentences.append(sentence)
    return build_semantic_descriptors(all_sentences)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    vec1 = {}
    vec2 = {}
    best_score = -1
    best_choice = choices[0]
    for choice in choices:
        vec2 = semantic_descriptors[choice]
        vec1 = semantic_descriptors[word]
        score = similarity_fn(vec1, vec2)
        if score > best_score:
            best_score = score
            best_choice = choice
    return best_choice

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    lines = []
    correct_answers = 0
    with open(filename, "r", encoding = "latin1") as f:
        for line in f:
            line = line.strip().split()
            lines.append(line)
    question_correct_answer = {}
    question_choice = {}
    for i in range(len(lines)):
        question_correct_answer.update({lines[i][0]: lines[i][1]})
        question_choice.update({lines[i][0]: lines[i][2:]})
    for question, choices in question_choice.items():
        if most_similar_word(question, choices, semantic_descriptors, similarity_fn) == question_correct_answer[question]:
            correct_answers += 1
    return correct_answers, len(question_choice)

if __name__ == "__main__":
    pass



