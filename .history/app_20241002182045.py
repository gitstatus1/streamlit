import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

computer_gif = load_lottie("https://lottie.host/b085e3a3-cfe4-4224-aa33-a1e48ae75172/js8SdwJw0t.json")

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
        st_lottie(computer_gif, height = 300, key = 'coding')
