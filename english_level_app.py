import streamlit as st
from PIL import Image
import pandas as pd
import joblib
import requests
from io import BytesIO

# header and cover of the app

st.set_page_config(page_title='English Movie Language Level Classifier',
                   page_icon=':clapper:', layout='wide',
                   initial_sidebar_state='auto')

MODEL_FILE = ./best_model.pkl'.
MOVIES_DATA_URL = 'https://api.themoviedb.org/3/search/movie'
movies_df = 'https://github.com/mamaewapolya/english_level_prediction/main/df_movies_raw.csv'

# loading the model
try:
    with open(MODEL_FILE, 'rb') as f:
        model = joblib.load(MODEL_FILE)
except:
    st.write('Error loading the model file.')

# loading an icon

response = requests.get('https://github.com/mamaewapolya/english_level_prediction/main/eng_movies.jpg')
cover_image = Image.open(BytesIO(response.content))
st.image(cover_image, use_column_width=True)

# setting header
st.title('English Movie Language Level Classifier')

# setting subheader
st.write('This application helps English learners to determine the level of a movie difficulty by subtitles. Just enter the name of a movie and embrace the magic of AI.')

# movie input box
movie_name = st.text_input('Enter the name of a movie')

if movie_name:
    # checking if we have a movie in a list
    movie_info = movies_df[movies_df['Movie'] == movie_name].iloc[0]
    if not movie_info:
        st.write('Sorry, we do not have subtitles for this movie. Please try another one.')
    else:
        # getting level of proficiency
        level = predict_level(movie_name)
        
        if level == 'A1':
            color = 'green'
        elif level == 'A2':
            color = 'orange'
        elif level == 'B1':
            color = 'red'
        elif level == 'B2':
            color = 'purple'
        elif level == 'C1':
            color = 'blue'
        elif level == 'C2':
            color = 'black'
        else:
            color = 'gray'
        st.subheader(f'Level of your movie: ')
        st.subheader(f'{level}',  style=f'color:{color};font-size:30px')
else:
    st.write('Please enter a movie name.')
