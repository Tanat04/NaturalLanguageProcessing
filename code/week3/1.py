# Thanarit Kanjanmetawat ID:6410322 NLP Workshop3
import nltk
from nltk.corpus import reuters
import random

# Concatenating all Reuters documents into one string
text = " ".join(reuters.words())

all_words = nltk.word_tokenize(text)
bigram = list(nltk.bigrams(all_words))

unique_word = {}

# Finding Unique Words
for w in all_words:
    if w in unique_word:
        unique_word[w] += 1
    else:
        unique_word[w] = 1

unique_word_prob = {}
# Calculating Probability
for w in unique_word:
    unique_word_prob[w] = unique_word.get(w) / len(all_words)

unique_bigram = {}
# Finding Unique Bigram
for b in bigram:
    if b in unique_bigram:
        unique_bigram[b] += 1
    else:
        unique_bigram[b] = 1

print(unique_bigram)
unique_bigram_prob = {}
# Calculating Probability
for b in unique_bigram:
    if (x := unique_bigram.get(b)) is None:
        unique_bigram_prob[b] = 0
    else:
        unique_bigram_prob[b] = x / unique_word.get(b[0])


sentence_length = 20
result = list(random.choices(list(unique_bigram_prob.keys()),
              weights=list(unique_bigram_prob.values()), k=sentence_length//2))
result_sentence = ""
for r in result:
    for a in r:
        result_sentence += a + " "

print(result_sentence.title())
