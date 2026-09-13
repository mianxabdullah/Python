# 🎬 Movie Recommendation System

A movie recommendation system built using **Unsupervised Learning techniques** including **PCA**, **K-Means Clustering**, and **Cosine Similarity**.

The system groups similar movies together and recommends movies from the same cluster based on feature similarity.

---

## Features

- Movie feature engineering
- Dimensionality reduction using PCA
- Movie clustering using K-Means
- Similarity-based recommendations
- Interactive Streamlit application
- Visualizations for PCA and clustering analysis

---

## Techniques Used

- StandardScaler
- Principal Component Analysis (PCA)
- K-Means Clustering
- Elbow Method
- Silhouette Score
- Cosine Similarity

---

## 📂 Project Structure

```text
Movie_Recommendation/

│
├── data/
│   ├── raw/
│   │   ├── movies.csv
│   │   └── ratings.csv
│   │
│   └── processed/
│       └── movie_features.csv
│
├── models/
│   ├── scaler.pkl
│   ├── pca.pkl
│   └── kmeans.pkl
│
├── outputs/
│   ├── pca_features.csv
│   ├── clustered_movies.csv
│   ├── pca_variance.png
│   ├── pca_movies.png
│   ├── elbow_method.png
│   ├── silhouette_scores.png
│   └── clustered_movies.png
│
├── notebooks/
│   ├── preprocessing.ipynb
│   ├── feature_eng.ipynb
│   ├── scaling_pca.ipynb
│   ├── clustering.ipynb
│   └── recommendation.ipynb
│   
├── recommendation.py
├── app.py
│
├── requirements.txt
└── README.md
```

---

## Workflow

```text
Movies + Ratings
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Standard Scaling
        │
        ▼
PCA (95% Variance Retained)
        │
        ▼
K-Means Clustering
        │
        ▼
Elbow Method
        │
        ▼
Silhouette Analysis
        │
        ▼
Movie Clusters
        │
        ▼
Cosine Similarity
        │
        ▼
Recommendations
```

---

## Visualizations

- PCA Explained Variance
- Movies in PCA Space
- Elbow Method
- Silhouette Scores
- Cluster Visualization

---

## Streamlit App

Run the application locally:

```bash
streamlit run app.py
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your_username/Movie_Recommendation.git

cd Movie_Recommendation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Streamlit:

```bash
streamlit run app.py
```

---

## Dataset

MovieLens Dataset

Contains:

- Movies
- Ratings
- Genres
- User interactions

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Streamlit
- Joblib

---

## Future Improvements

- Movie Posters (TMDB API)
- User-based recommendations
- Hybrid Recommendation Systems
- Deployment on Streamlit Cloud
- Recommendation explanations

---

##  Author

Abdullah Ayub

Built as a personal project to explore **Unsupervised Learning** and **Recommendation Systems**.