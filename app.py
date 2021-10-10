import streamlit as st
import joblib
import pandas as pd
import requests

st.set_page_config(page_title = "Movies Recommender",layout='wide')

@st.cache(suppress_st_warning=True)
def load_data():
    movies = pd.read_csv("dataset/final_dataset.csv")
    
    similarity_saved = joblib.load("cosine_similarity.joblib")
    return movies,similarity_saved 

movies,similarity_saved = load_data()
movies_list = movies['title'].values
#st.write(movies['title'].values)
@st.cache(suppress_st_warning=True)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=d0a220bafccbd55a3b2286a0b7cf6e0e&language=en-US"
    response = requests.get(url)
    data = response.json()
    print(data)
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


@st.cache(suppress_st_warning=True)
def recommend(movie_name):
    movie_index = movies[ movies['title']== movie_name ].index[0]
    distances = similarity_saved[movie_index]
    movies_list = sorted( list(enumerate(distances)),reverse =True ,key = lambda x:x[1]  ) [1:11]
    recommend_movies = []
    movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        #print(i[0])
        #explained below
        #print(movies.iloc[ i[0] ].title)
        recommend_movies.append( movies.iloc[i[0]].title )
        #fetch poster using API
        movies_posters.append(fetch_poster(movie_id))
    return recommend_movies,movies_posters

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "",
    (movies_list)
)
if st.button("Recommend"):
    #st.write(selected_movie_name)
    movies_recommeded,movies_posters = recommend(selected_movie_name)
    #for movie in movies_recommeded:
        #st.text(movie)
    image_section1 = st.container()
    image_section2 = st.container()
    cols = st.columns(5)
    cols2 = st.columns(5)
    counter = 1
    step_1 = 0
    step = 0
    #st.text(len(movies_recommeded))
    # st.text(list(enumerate(movies_recommeded)))
    for index,name in enumerate(movies_recommeded):
        with image_section1:
            if counter <= 5:
                with cols[step_1]:
                
                    st.image(movies_posters[index])
                    st.text(name)
                    step_1 += 1
        if counter>5:
            with image_section1:
                with cols2[step]:
            
                    st.image(movies_posters[index])
                    st.text(name)
                    step += 1
        counter += 1
        #print(step_1)
        #print(step_1)
        
        
   