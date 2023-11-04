import re

sentence = "I have so much fun. Dayamm!"
cleanedSentence = re.sub('[.!]', '', sentence)

words = cleanedSentence.split()

print(words)
