from nltk.corpus import movie_reviews
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt


def evaluate_model(test_size):
    print(f"Train/Test Split Ratio: {1 - test_size}:{test_size}")

    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]

    train, test = train_test_split(
        documents, test_size=test_size, random_state=42)

    # Feature Extraction
    x_train = [' '.join(words) for (words, label) in train]
    x_test = [' '.join(words) for (words, label) in test]
    y_train = [label for (words, label) in train]
    y_test = [label for (words, label) in test]

    count_vec = TfidfVectorizer(min_df=10, token_pattern=r'[a-zA-Z]+')

    # count_vec = CountVectorizer()
    x_train_bow = count_vec.fit_transform(x_train)

    # Model training
    model = GaussianNB()
    model.fit(x_train_bow.toarray(), y_train)

    # Evaluation
    x_test_bow = count_vec.transform(x_test)
    accuracy = model.score(x_test_bow.toarray(), y_test)
    print("Accuracy:", accuracy)
    y_predict = model.predict(x_test_bow.toarray())
    print(classification_report(y_test, y_predict))

    cm = confusion_matrix(y_test, y_predict)
    print(cm)

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm, display_labels=model.classes_)
    disp.plot()
    plt.show()
    print("--------------------------------------")


# Test with different train/test splitting ratios
evaluate_model(test_size=0.3)  # 70:30
evaluate_model(test_size=0.2)  # 80:20
evaluate_model(test_size=0.1)  # 90:10
