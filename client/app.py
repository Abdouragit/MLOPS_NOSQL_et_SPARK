import streamlit as st
import requests

st.title("My beautiful App")
button_clicked = st.button("Add a fruit")

## write fruits
fruit = st.text_input('Fruit name', 'Apple')

if button_clicked:
    st.write("It worked")
    st.balloons()
    requests.get(url=f'http://localhost:8000/add/{fruit}')
    # requests.post(
    #     url='http://localhost:8000/add',
    #     json={'fruit': fruit}
    # )



## get fruits

button_clicked = st.button("Get fruit list")

if button_clicked:
    st.write("Get your fruits")
    # st.balloons()
    response = requests.get(url='http://localhost:8000/list')
    st.write(response.json())
