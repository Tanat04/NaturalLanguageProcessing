from nltk.corpus import movie_reviews
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

print(len(movie_reviews.fileids()))
print(movie_reviews.categories())
print(movie_reviews.words()[:50])
print(movie_reviews.fileids()[:10])
print()

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# print(documents[0])
print(len(documents))
print()

distribution = Counter([label for (words, label) in documents])
print(distribution)

train, test = train_test_split(documents, test_size=0.1)
print(Counter([label for (words, label) in train]))
print(Counter([label for (words, label) in test]))
print()


# Feature Extraction
x_train = [' '.join(words)for (words, label) in train]
x_test = [' '.join(words)for (words, label) in test]
y_train = [label for (words, label) in train]
y_test = [label for (words, label) in test]

# print(x_test)
# print(y_test)
# print()

# Feature Extraction
# count_vec = TfidfVectorizer(min_df=10, token_pattern=r'[a-zA-Z]+')
count_vec = CountVectorizer()
x_train_bow = count_vec.fit_transform(x_train)

# Model training
model = GaussianNB()
model.fit(x_train_bow.toarray(), y_train)

# Evaluation
x_test_bow = count_vec.transform(x_test)
accuracy = model.score(x_test_bow.toarray(), y_test)
print("Accuracy:", accuracy)

y_predict = model.predict(x_test_bow.toarray())
precision = precision_score(y_test, y_predict, average='weighted')
recall = recall_score(y_test, y_predict, average='weighted')
print("Precision:", precision)
print("Recall:", recall)
f1 = f1_score(y_test, y_predict, average='weighted')
print("f1_score: ", f1)

cm = confusion_matrix(y_test, y_predict)
print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm, display_labels=model.classes_)

disp.plot()
plt.show()
