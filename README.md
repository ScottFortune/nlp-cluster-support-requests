# NLP Clustering Support Tickets

This projects simulates a real-world use case I worked on during my time at Fidelity: clustering service tickets to identify common issues and reduce support overhead.

## Overview

- Input: Simulated service ticket descriptions
- Preprocessing: Cleaning and tokenizing text
- Vectorization: TF-IDF and/or embeddings
- Clustering: KMeans, HDBSCAN, etc.
- Output: Cluster summaries and visualizations

This repo demonstrates the core techniques and logic used while respecting data confidentiality.

## Notebooks

| Notebook | Description |
|----------|-------------|
| 01_preprocessing | Clean and prepare ticket descriptions |
| 02_vectorization | Convert text to numerical features |
| 03_clustering | Apply clustering algorithms and analyze output |
| 04_visualization | Plot and interpret clusters with tools like t-SNE/UMAP |

## 🧠 Techniques Used

- NLP preprocessing with `nltk` / `spaCy`
- Vectorization: TF-IDF, Sentence Transformers
- Clustering: KMeans, DBSCAN, HDBSCAN
- Visualization: UMAP, t-SNE, seaborn

## 📌 Why It Matters

By clustering support tickets, we can:
- Reduce duplicate issue handling
- Identify root causes more effectively
- Optimize IT and support workflows

## 🛡️ Disclaimer

This is a personal project based on techniques used at Fidelity. All data is mock and generated for educational/demo purposes.

## 🚀 Setup

```bash
pip install -r requirements.txt
```