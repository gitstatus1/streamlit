import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

computer_gif = "https://lottie.host/embed/3a31d5cc-3e00-4320-ab72-4c2301b1eae1/Zi9tWzaDKu.json"

#Set up the webpage 
st.set_page_config(page_title = "My Webpage", page_icon= ":black_square_button:", layout = 'wide')

# header section
with st.container():
    st.subheader("Hi, I am Eric :wave:")
    st.title("An Data and AI Enthusiast")
    st.write("I am passionate about finding ways to use Python and ")
    st.write("[✨Checkout My LinkedIn✨](https://www.linkedin.com/in/ericlau2000/)")


#places to get free gifs lottiefiles.com 
# what i do
with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What I Do")
        st.write("##")
        st.write(
            '''
            I am a data driven person.
            i love dota and shit
            '''
        )

    with right_col:
