import streamlit as st


#Set up the webpage 
st.set_page_config(page_title = "My Webpage", page_icon= ":black_square_button:", layout = 'wide')

# header section
with st.container():
    st.subheader("Hi, I am Eric :wave:")
    st.title("An Data and AI Enthusiast")
    st.write("I am passionate about finding ways to use Python and ")
    st.write()
# what i do
with st.container():
    st.write("---")
    left_col, right_col = set.columns(2)
    with left_col:
        st.header("What I Do")
        st.write("##")
        st.write(
            '''
            I am a data driven person.
            i love dota and shit
            '''
        )
