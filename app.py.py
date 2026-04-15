import streamlit as st
import pickle
import pandas as pd

# load files
movies = pickle.load(open("movies.pkl", "rb"))
content_sim = pickle.load(open("content.pkl", "rb"))
cf_sim = pickle.load(open("cf.pkl", "rb"))


def recommend(movie_name):

    movie_name = movie_name.lower()
    movies["title_lower"] = movies["title"].str.lower()

    if movie_name not in movies["title_lower"].values:
        return ["Movie not found"]

    idx = movies[movies["title_lower"] == movie_name].index[0]

    content_scores = list(enumerate(content_sim[idx]))

    try:
        cf_scores = list(enumerate(cf_sim[idx]))
    except:
        cf_scores = []

    hybrid = []

    for i in range(len(content_scores)):

        c_score = content_scores[i][1]

        if i < len(cf_scores):
            cf_score = cf_scores[i][1]
        else:
            cf_score = 0

        final = (0.6 * c_score) + (0.4 * cf_score)
        hybrid.append((i, final))

    hybrid = sorted(hybrid, key=lambda x: x[1], reverse=True)

    result = []
    for i in hybrid[1:6]:
        result.append(movies.iloc[i[0]].title)

    return result


# UI
st.title("🎬 Advanced Movie Recommender System")

selected = st.selectbox("Select a movie", movies["title"].values)

if st.button("Recommend"):

    recs = recommend(selected)

    st.subheader("Top Recommendations")

    for m in recs:
        st.write(m)