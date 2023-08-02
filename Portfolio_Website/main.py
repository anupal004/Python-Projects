import streamlit as st

st.set_page_config(layout="wide")
# this method makes the browser page wide, and we can also write "centered" to make center alignment

col1, col2, col3 = st.columns(3)
# using this method to center the profile photo.
with col1:
    st.write(' ')

with col2:
    st.image("Portfolio_Website/images/profile.png")

with col3:
    st.write(' ')

st.markdown("<h1 style='text-align: center; color: grey;'>Anupal Deuri Bharali</h1>", unsafe_allow_html=True)
# using this command will align the text at the center.

st.info("""I am an Electronics and Telecommunication Engineering undergraduate, from Assam Engineering College situated 
in Guwahati, Assam. I am particularly fascinated with
Science and Technology and I am also interested in designing, coding, and making digital illustrations in my free time. 
I have a systematic and well planned proposition in every job that I undertake. This portfolio showcases my work as an 
Python Programmer.""")

st.write("""Below you can find some of the Python Projects I have built so far!""")