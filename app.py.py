import streamlit as st
import pickle
import pandas as pd

# Load data
movies = pickle.load(open("movies.pkl", "rb"))
content_similarity = pickle.load(open("content.pkl", "rb"))
movie_similarity_cf = pickle.load(open("cf.pkl", "rb"))

# Recommend function
def recommend(movie_name):
    
    movie_name = movie_name.lower()
    movies['title_lower'] = movies['title'].str.lower()
    
    if movie_name not in movies['title_lower'].values:
        return ["Movie not found"]
    
    idx = movies[movies['title_lower'] == movie_name].index[0]
    
    content_scores = list(enumerate(content_similarity[idx]))
    
    # Try CF safely
    try:
        cf_scores = list(enumerate(movie_similarity_cf[idx]))
    except:
        cf_scores = []
    
    hybrid_scores = []
    
    for i in range(len(content_scores)):
        
        content_score = content_scores[i][1]
        
        if i < len(cf_scores):
            cf_score = cf_scores[i][1]
        else:
            cf_score = 0
        
        score = (0.6 * content_score) + (0.4 * cf_score)
        hybrid_scores.append((i, score))
    
    hybrid_scores = sorted(hybrid_scores, key=lambda x: x[1], reverse=True)
    
    result = []
    for i in hybrid_scores[1:6]:
        result.append(movies.iloc[i[0]].title)
    
    return result


# UI
st.title("🎬 Advanced Movie Recommender System")

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie", movie_list)

if st.button("Recommend"):
    results = recommend(selected_movie)
    
    st.subheader("Top Recommendations:")
    
    for movie in results:
        st.write(movie)