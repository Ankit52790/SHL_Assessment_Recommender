# recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

class Recommender:
    def __init__(self, user_path="data/users.csv", assessment_path="data/assessments.csv"):
        self.user_path = user_path
        self.assessment_path = assessment_path
        self.users = None
        self.assessments = None
        self.recommendations = {}

    def load_data(self):
        print("[INFO] Loading data...")
        self.users = pd.read_csv(self.user_path)
        self.assessments = pd.read_csv(self.assessment_path)

        self.assessments["skill_area"] = self.assessments["skill_area"].fillna("")
        self.users["interests"] = self.users["interests"].fillna("")

    def recommend_assessments(self, top_n=3):
        print("[INFO] Generating recommendations...")
        vectorizer = TfidfVectorizer()
        assessment_vectors = vectorizer.fit_transform(self.assessments["skill_area"])
        user_vectors = vectorizer.transform(self.users["interests"])

        similarity_matrix = cosine_similarity(user_vectors, assessment_vectors)

        for i, user_id in enumerate(self.users["user_id"]):
            top_indices = similarity_matrix[i].argsort()[-top_n:][::-1]
            recommended = self.assessments.iloc[top_indices]["name"].tolist()
            self.recommendations[user_id] = recommended

    def save_recommendations(self, output_file="user_recommendations.json"):
        print("[INFO] Saving recommendations to JSON...")
        with open(output_file, "w") as f:
            json.dump(self.recommendations, f, indent=2)

    def print_recommendations(self):
        print("\n[INFO] Final Recommendations:")
        for user_id, recs in self.recommendations.items():
            print(f"User: {user_id} -> Recommended Assessments: {recs}")
