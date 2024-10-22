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
st.markdown("<style>.text{font-size:25px !important;}</style>", unsafe_allow_html=True)
st.markdown("<style>.title{font-size:68px !important;}</style>", unsafe_allow_html=True)
st.markdown("<style>.subtitle{font-size:45px !important;}</style>", unsafe_allow_html=True)


# header section
with st.container(): #key = "top container"
    col1, col2 = st.columns(2)

    with col2:
        st_lottie(robot_gif, key = 'robot', height = 500, width = 500)

    with col1:
        st.markdown('<p class="title">Hi, I am Eric 👋</p>', unsafe_allow_html= True)
        st.subheader("Data and AI Enthusiast")      
        st.markdown('''<p class="text">I am passionate about harnessing data science and AI to solve real-world problems and improve quality of life. 
                I am driven by the potential of technology to innovate across industries and create meaningful impact in the society.</p>''', unsafe_allow_html= True)
        st.markdown('''<p class="text">
            As a problem solver with a keen eye for detail, I approach challenges by uncovering patterns and insights within data. 
            Leveraging the power of AI and analytics, data can be transformed into compelling narratives and help organisations innovate.
            I like playing around with AI technology and work on fun projects. Please have a look!</p>''', unsafe_allow_html=True)


        
with st.container(): #key = Projects
    st.write("---")
    left, right = st.columns(2)
    with left:
        st.markdown('<div style="text-align:right"><p class="subtitle">Projects</p></div>', unsafe_allow_html= True)
        st.write("##")

with st.container(): #key = Image Generation Project
    left_col, right_col = st.columns(2)
    with left_col:
        st.subheader("Image Generation with ControlNet")
        st.markdown('''
                    <p class="text">
                    ControlNet is a neural network used in conjunction with the Stable Diffusion model to condition image generation with and added complexity.
                    This project is a fun image generation project utilising advanced AI image generation techniques to create customised visuals based on user inputs.
                    </p>
                    ''',
                      unsafe_allow_html=True)
        st.write("##")
        st.write('[✨See Project Link✨](https://colab.research.google.com/drive/1MNslw2EyoMf1QSsPnBT_FaGDAYhRBbkD?usp=sharing)')
        st.markdown(f'<p style="font-size:20px;">✨<a href="https://colab.research.google.com/drive/1-FdBnXT1b5TipWuWlfAq5H2NZVTz0sx4?usp=sharing" target="_blank">See Project Link✨</a></p>',
        unsafe_allow_html=True)
    right_col.image("controlnet.png", caption='Transforming "The Great Wave" artwork into different styles', width = 500)
    st.write("##")


with st.container(): #key= "Tank Pressure"
    left_col, right_col = st.columns(2, gap = "large")
    with left_col:
        st.subheader("Tank Pressure Prediction")
        st.markdown('''
                    <p class="text">
                    A regression project focused on predicting the target pressure of a tank based on various input features using statistical and machine learning
                    techniques. After developing the machine learning models, the goal of the project aims to provide explainable and interpretable insights of impact of different features on the target variable.
                    </p>
                    ''',
                      unsafe_allow_html=True)
        st.write("##")
        st.markdown(f'<p style="font-size:20px;">✨<a href="https://colab.research.google.com/drive/1-FdBnXT1b5TipWuWlfAq5H2NZVTz0sx4?usp=sharing" target="_blank">See Project Link✨</a></p>',
        unsafe_allow_html=True)
    right_col.image("watertank.png", width = 400)


with st.container(): #key = Contacts
    st.write("---")
    left, right  = st.columns(2)
    with left:
        st.markdown('<div style="text-align:right"><p class="subtitle">Contacts</p></div>', unsafe_allow_html= True)

with st.container(): #key = linkedin container
    left, right = st.columns(2)
    with left:
        st.markdown(
            f'''
            <p class="text" style="display:inline-block;">
            <img src="data:image/png;base64,{base64.b64encode(open("textbubble.png", "rb").read()).decode()}" width="50">
               Socials
            </a>
            </p>''' ,
            unsafe_allow_html=True,
        )
        st.markdown(
            f'''
            <a href="https://www.linkedin.com/in/ericlau2000/">
            <img src="data:image/png;base64,{base64.b64encode(open("linkedin.png", "rb").read()).decode()}" width="50">
            </a><p class="text" style="display:inline-block;">Linkedin</p>
            ''' ,
            unsafe_allow_html=True
        )
    with right:
        st.markdown(
            f'''
            <p class="text" style="display:inline-block;">
            <img src="data:image/png;base64,{base64.b64encode(open("email.png", "rb").read()).decode()}" width="50">
              Email
            </a>
            </p>''' ,
            unsafe_allow_html=True,
        )

        st.markdown(
            '''
            <p class="text" style="display:inline-block;">
            ericlau2000@hotmail.com  
            </p>'''
        ,unsafe_allow_html=True,
        )
