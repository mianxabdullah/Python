import streamlit as st
from recommendation import recommend

# Page settings
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

# Sidebar
st.sidebar.title("About")

st.sidebar.markdown("""
###  **Movie Recommendation System**

This project uses:

- **PCA** for dimensionality reduction
- **K-Means Clustering** for grouping similar movies
- **Cosine Similarity** for recommendations

### Features
- Unsupervised Learning  
- PCA  
- K-Means  
- Similar Movie Suggestions
""")

# Main UI
st.title("Movie Recommendation System")

st.caption(
    "Discover movies using PCA, K-Means Clustering and Cosine Similarity"
)

movie = st.text_input(
    "Enter movie name",
    placeholder="Toy Story"
)

n = st.slider(
    "Recommendations",
    5,
    20,
    10
)

if st.button("Recommend"):

    recs = recommend(movie, n)

    if len(recs) == 0:

        st.error("Movie not found")

    else:

        st.success(f"Top {n} Recommendations")

        for i, m in enumerate(recs, 1):

            st.markdown(f"**{i}.** {m}")