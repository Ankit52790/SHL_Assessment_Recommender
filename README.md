# SHL Assessment Recommendation Engine

This project recommends SHL assessments to users based on their skills and interests using content-based filtering.

## 📁 Dataset
- `data/assessments.csv`: Contains SHL assessments along with their skill areas.
- `data/users.csv`: Contains user IDs and their declared interests.

## 🧠 How It Works
1. Loads and preprocesses the `skill_area` and `interests` fields.
2. Uses **TF-IDF Vectorization** to convert text into feature vectors.
3. Computes **cosine similarity** between each user and available assessments.
4. Recommends the top 3 most relevant assessments per user.
5. Saves the recommendations in `user_recommendations.json`.

## 🚀 How to Run

### ✅ Prerequisites
- Python 3.x installed on your system.
- Required Python packages listed in `requirements.txt`.

### 🔧 Setup
Clone the project and navigate to the folder:

```bash
git clone https://github.com/Ankit52790/SHL_Assessment_Recommender.git
cd SHL_Assessment_Recommender
