# Main entry point for SHL Recommendation Engine

from recommender import Recommender  # Ensure this import is correct

def run_recommendations():
    print("Starting SHL Assessment Recommendation Engine...")
    recommender = Recommender()  # Instantiate the Recommender class properly
    recommender.load_data()
    recommender.recommend_assessments()
    recommender.save_recommendations()
    recommender.print_recommendations()

if __name__ == "__main__":
    run_recommendations()
