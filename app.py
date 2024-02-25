import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=bb58f107b086eabc6b574e59dc624d58&language=en-US%27'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movie = []
    recommend_movie_poster = []
    for j in movies_list:
        movie_id = movies.iloc[j[0]].movie_id
        #fetch poster from api
        #  my api : bb58f107b086eabc6b574e59dc624d58
        recommend_movie.append(movies.iloc[j[0]].title)
        recommend_movie_poster.append(fetch_poster(movie_id))

    return recommend_movie, recommend_movie_poster
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.text(names[0])


    with col2:
        st.image(posters[1])
        st.text(names[1])


    with col3:
        st.image(posters[2])
        st.text(names[2])
    with col4:

        st.image(posters[3])
        st.text(names[3])
    with col5:
        st.image(posters[4])

        st.text(names[4])




