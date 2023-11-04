# Tanat Arora, ID: 6410381

import nltk
from nltk.probability import FreqDist
import random
from nltk.corpus import reuters

sentence = "I am Sam Sam am I do not like green eggs and ham"
tokens = nltk.word_tokenize(sentence)

freq_dist = FreqDist(tokens)
total_words = len(tokens)

for word in set(tokens):
    probability = freq_dist[word] / total_words
    print(f"Probability of '{word}' appearing next: {probability}")

# Genarating 20 words text

text = " ".join(reuters.words())

tokens = nltk.word_tokenize(text)
total_words = len(tokens)
freq_dist = FreqDist(tokens)

generated_sequence = []

current_word = random.choice(tokens)
generated_sequence.append(current_word)

for _ in range(19):
    next_candidates = [word for word in set(
        tokens) if freq_dist[word] / total_words > freq_dist[current_word] / total_words]

    if next_candidates:
        next_word = random.choice(next_candidates)
    else:
        next_word = random.choice(tokens)

    current_word = next_word
    generated_sequence.append(current_word)

generated_text = ' '.join(generated_sequence)
print("Generated Sequence:")
print(generated_text)
