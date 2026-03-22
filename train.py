import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

MODEL_PATH = os.path.join("models", "model.pkl")


def train_and_save_model(random_state: int = 42):
    X, y = make_classification(n_samples=1000, n_features=10, n_informative=6, n_redundant=2, random_state=random_state)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(clf, MODEL_PATH)
    print(f"Trained model saved to {MODEL_PATH} — accuracy: {acc:.4f}")
    return MODEL_PATH, acc


if __name__ == "__main__":
    train_and_save_model()
