# Tanat Arora ID: 6410381

import nltk
import random
from nltk.probability import FreqDist
from nltk.corpus import reuters

# Concatenate all Reuters documents into one string
text = " ".join(reuters.words())

tokens = nltk.word_tokenize(text)
bigrams = list(nltk.bigrams(tokens))

unique_word = FreqDist(tokens)
unique_bigram = FreqDist(bigrams)

generated_sequence = []

current_word = random.choice(tokens)
generated_sequence.append(current_word)

for _ in range(19):
    next_candidates = [
        b for b in unique_bigram if unique_bigram[b] >= unique_word[current_word] * 0.3]

    if next_candidates:
        next_bigram = random.choice(next_candidates)
        next_word = next_bigram[1]
    else:
        next_word = random.choice(tokens)

    current_word = next_word
    generated_sequence.append(current_word)

generated_text = ' '.join(generated_sequence)
print("Generated Sequence:")
print(generated_text)
