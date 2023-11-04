from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello Mr.Bond. We've got a misson for you. Here're the details"


all_words = word_tokenize(text)
bigrams = list(nltk.bigrams(all_words))
print(f"Bigrams: {bigrams}")

trigrams = list(nltk.trigrams(all_words))
print(f"Trigrams: {trigrams}")

tags = nltk.pos_tag(all_words)
print("Tags: ", tags)


wordList = ["play", "played", "playing", "is", "am", "are", "be", "mouse"]
print("WordList: ", wordList)

lemmatizer = WordNetLemmatizer()
lemmaVerbs = [lemmatizer.lemmatize(word, pos=wordnet.VERB)
              for word in wordList]

print("LemmaVerbsr: ", lemmaVerbs)

lemmaNouns = [lemmatizer.lemmatize(word, pos=wordnet.NOUN)
              for word in wordList]

print("lemmaNouns: ", lemmaNouns)
