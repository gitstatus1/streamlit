import streamlit as st
import requests
from streamlit_lottie import st_lottie
import base64

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# assets 
# places to get free gifs lottiefiles.com 

robot_gif = load_lottie("https://lottie.host/98bf9519-e06c-44c4-a23a-e3cf1a423dbb/GvgWI6d56p.json")

#Set up the webpage 
st.set_page_config(page_title = "Eric Lau", page_icon= ":black_square_button:", layout = 'wide')
#load css
local_css("style/style.css")

#markdown styles
st.markdown("<style>.text{font-size:22px !important;}</style>", unsafe_allow_html=True)
st.markdown("<style>.title{font-size:60px !important;}</style>", unsafe_allow_html=True)

# header section
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st_lottie(robot_gif, height = 300, key = 'robot')

    with col2:
        st.markdown('<p class="title">Hi, I am Eric 👋</p>', unsafe_allow_html= True)
        st.subheader("Data and AI Enthusiast")
        st.markdown('<p class="text">I am passionate about harnessing data science and AI to solve real-world problems and improve quality of life. I am driven by the potential of technology to innovate across industries and create meaningful impact in the society.</p>', unsafe_allow_html= True)

    with col3:
       st.markdown(
            """Linkedin: <a href="https://www.linkedin.com/in/ericlau2000/">
            <img src="data:image/png;base64,{}" width="50">
            </a>""".format(
                base64.b64encode(open("linkedin.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )

with st.container():
    st.write("---")
    _, mid,  _ = st.columns(3)
    with mid:
        st.header("What I Do")

# what i do
with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What I Do")
        st.markdown('''<p class="text">
                    As a problem solver with a keen eye for detail, I approach challenges by uncovering patterns and insights within data. 
                    Leveraging the power of AI and analytics, data can be transformed into compelling narratives and help organisations innovate.</p>''', unsafe_allow_html=True)
        st.markdown('''<p class="text">
                    I like playing around with AI technology and have fun projects have a look!</p>''', unsafe_allow_html=True)

with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("Projects")
        st.subheader("Image Generation with ControlNet")
        st.markdown('<p class="text">A fun image generation project utilizing advanced AI techniques to create customized visuals based on user inputs.</p>', unsafe_allow_html=True)
        st.write("[Project Link](https://google.com)")
    with right_col:
        st.write('image here')

#contact me
# with st.container():
#     st.write('---')
#     st.write('##')
#     st.subheader('Send me a message!')
#     contact_form = """
#     <form action = "https://formsubmit.co.codingisfun.test.user@gmail.com" method="POST">
#         <input type="hidden" name="_captcha" value="false">
#         <input type="text" name="name" placeholder="Your name" required>
#         <input type="email" name="email" placeholder="Your email" required>
#         <textarea name="message" placeholder="Your message here" required></textarea>
#         <button type="submit">Send</button>
#     </form>
#     """
#     with left_col:
#         st.markdown(contact_form, unsafe_allow_html=True)
#     with right_col:
#         st.empty()
        