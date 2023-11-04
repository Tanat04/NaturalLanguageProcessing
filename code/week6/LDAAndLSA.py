import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import normalize
import csv
import matplotlib.pyplot as plt


def plot_top_words(model, feature_names, n_top_words, title):
    fig, axes = plt.subplots(1, 5, figsize=(
        45, 15), gridspec_kw={'hspace': 0.3})
    axes = axes.flatten()
    for topic_idx, topic in enumerate(model.components_):
        top_features_ind = topic.argsort()[: -n_top_words - 1: -1]
        top_features = [feature_names[i] for i in top_features_ind]
        weights = topic[top_features_ind]

        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f"Topic {topic_idx + 1}", fontdict={"fontsize": 15})
        ax.invert_yaxis()
        ax.tick_params(axis="both", which="major", labelsize=10)
        for i in "top right left".split():
            ax.spines[i].set_visible(False)
    fig.suptitle(title, fontsize=18)

    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.show()


# Sample training data (replace this with your actual dataset)
training_data = []
max_rows = 10000  # Maximum number of rows to read from the CSV file

with open('abcnews-date-text.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for idx, row in enumerate(csv_reader):
        if idx >= max_rows:
            break
        # Assuming headline_text is in the second column
        training_data.append(row[1])

# Step 1: Preprocess your text data and create a bag-of-words representation
# Specify the stop words and set max_features
vectorizer = CountVectorizer(stop_words='english', max_features=50000)
X = vectorizer.fit_transform(training_data)

# Step 2: Train the LDA model with 5 topics
num_topics = 5
lda_model = LatentDirichletAllocation(n_components=num_topics, random_state=99)
lda_model.fit(X)

# Step 3: Print the top 10 words from each topic
feature_names = vectorizer.get_feature_names_out()

for topic_idx, topic in enumerate(lda_model.components_):
    top_words_indices = topic.argsort()[:-11:-1]  # Get indices of top 10 words
    top_words = [feature_names[i] for i in top_words_indices]
    print(f"Topic {topic_idx + 1}: {' '.join(top_words)}")

plot_top_words(lda_model, feature_names, n_top_words=10,
               title="Top 10 Words in Each LDA Topic")

print("\n================================")
# Step 4: Manually inspect LSA topics
vectorizer = CountVectorizer(stop_words='english', max_features=50000)
X = vectorizer.fit_transform(training_data)

lsa_model = TruncatedSVD(n_components=num_topics)
X_lsa = lsa_model.fit_transform(X)
X_lsa = normalize(X_lsa, norm='l2')  # Normalize the LSA vectors

# Step 5: Print the top 10 words from each topic
feature_names = vectorizer.get_feature_names_out()

for topic_idx in range(num_topics):
    topic = lsa_model.components_[topic_idx]
    top_words_indices = topic.argsort()[:-11:-1]  # Get indices of top 10 words
    top_words = [feature_names[i] for i in top_words_indices]
    print(f"Topic {topic_idx + 1}: {' '.join(top_words)}")

plot_top_words(lsa_model, feature_names, n_top_words=10,
               title="Top 10 Words in Each LSA Topic")
