import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# assets
robot_gif = load_lottie("https://lottie.host/98bf9519-e06c-44c4-a23a-e3cf1a423dbb/GvgWI6d56p.json")

#Set up the webpage 
st.set_page_config(page_title = "My Webpage", page_icon= ":black_square_button:", layout = 'wide')
#load css
local_css("style/style.css")


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
        st_lottie(robot_gif, height = 300, key = 'coding')

#contact me
with st.container():
    st.write('---')
        st.write('##')

    st.subheader('Send me a message!')
    contact_form = """
    <form action = "https://formsubmit.co.codingisfun.test.user@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st.empty()
        