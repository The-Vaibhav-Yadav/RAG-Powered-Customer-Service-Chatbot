import toml
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def load_data_from_toml(filepath):
    data = toml.load(filepath)["data"]
    queries = [item["query"] for item in data]
    labels = [item["label"] for item in data]
    return queries, labels

def train_classifier():
    queries, labels = load_data_from_toml("train_data/training_data.toml")
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(queries)
    classifier = LogisticRegression().fit(X, labels)
    
    return vectorizer, classifier

def classify_query(query, vectorizer, classifier):
    X = vectorizer.transform([query])
    return classifier.predict(X)[0]
