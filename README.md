# NLP Clustering Support Tickets

This projects simulates a real-world use case I worked on during my time at Fidelity: clustering service tickets to identify common issues and reduce support overhead.

## Dashboard
https://nlp-cluster-support-requests-m6iy6kp9f6pcxhidxue8fi.streamlit.app/

## Overview

- Input: Simulated service ticket descriptions
- Preprocessing: Text Cleaning, contraction expansion, lemmatization
- Vectorization: TF-IDF with dimensionality reduction (Truncated SVD)
- Clustering: KMeans (Baseline) and HDBSCAN
- Visualization: 2D UMAP projection
- Interactive Streamlit UI to explore clusters and keywords

This repo demonstrates the core techniques and logic used while respecting data confidentiality.

## Notebooks

| Notebook | Description |
|-------------------|-----------------------------------------------------------------------------|
| `01_preprocessing`| Clean, expand contractions, tokenize, remove stopwords, lemmatize text     |
| `02_vectorization`| TF-IDF vectorization and dimensionality reduction with Truncated SVD       |
| `03_clustering`   | Clustering with KMeans and HDBSCAN, UMAP projection, and keyword extraction |
| `app.py`          | Streamlit dashboard to explore clusters, tickets, and visualizations       |


## 🧠 Techniques Used

- Text preprocessing: `nltk`, regex, `contractions`
- Vectorization: `TfidfVectorizer`, `TruncatedSVD`
- Clustering: `KMeans`, `HDBSCAN`
- Dimensionality reduction: `UMAP`
- Visualization: `matplotlib`, `seaborn`, `Streamlit`

## 📌 Why It Matters

The dashboard allows you to:
- Explore clusters and their top keywords
- View raw tickets per cluster
- Visualize HDBSCAN clusters in UMAP space
- Filter and interactively explore the results

## 🛡️ Disclaimer

This is a personal project based on techniques used at Fidelity. All data is mock and generated for educational/demo purposes.

## 🚀 Setup

```bash
pip install -r requirements.txt
```

To run the dashboard locally:
```bash
streamlit run app.py
```