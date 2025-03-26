# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load Data ---
tickets_df = pd.read_csv("./data/ticket_clusters_hdbscan.csv")
keywords_df = pd.read_csv("./data/cluster_keywords_hdbscan.csv")
umap_df = pd.read_csv("./data/umap_projection.csv")

# --- Sidebar Controls ---
st.sidebar.title("Cluster Filter")
all_clusters = sorted(tickets_df["hdbscan_cluster"].unique())
selected_clusters = st.sidebar.multiselect("Select Clusters", all_clusters, default=all_clusters)

# --- Filter Data ---
filtered_df = tickets_df[tickets_df["hdbscan_cluster"].isin(selected_clusters)]

# --- Main View ---
st.title("🧠 Ticket Clustering Dashboard")
st.markdown("Explore clustered service tickets and understand common issues.")

# --- Cluster Summary Table ---
st.subheader("📌 Top Keywords per Cluster")
st.dataframe(keywords_df, use_container_width=True)

# --- UMAP Visualization ---
st.subheader("🗺️ UMAP Visualization of Clusters")

if "umap_x" in umap_df.columns and "umap_y" in umap_df.columns:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=umap_df[umap_df["hdbscan_cluster"].isin(selected_clusters)],
        x="umap_x",
        y="umap_y",
        hue="hdbscan_cluster",
        palette="tab10",
        alpha=0.8,
        ax=ax
    )
    ax.set_title("UMAP Projection of Ticket Clusters")
    ax.set_xlabel("UMAP 1")
    ax.set_ylabel("UMAP 2")
    ax.legend(title="Cluster", bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)
else:
    st.warning("UMAP coordinates not found in data.")

# --- Ticket Table ---
st.subheader("📋 Tickets")
st.dataframe(filtered_df[["ticket_id", "hdbscan_cluster", "description"]], use_container_width=True)

# Optional: Add search/filter or keyword tag cloud later