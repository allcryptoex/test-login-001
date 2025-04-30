import streamlit as st
from firebase_admin import auth

def app():
    #st.header(' UIL SPELLER!! ')
    
    header1, header2 = st.columns([0.75,3])
    with header1:
        container1 = st.container(border=True)   
        container1.image('logo.png', width=100)

    st.header(' :green[Getting Started!!]')

    st.write(' ### ')
    container = st.container(border=True)
    with container:
        col1, col2 = st.columns([4,2])
        col1.subheader(':green[**Subscribe to our newsletter**] ')
        col1.write('**Get our real time updates**')
        col2.text_input(label='', placeholder='Your Email')
        col2.button("Subscribe")

    st.write(' ### ')
    st.markdown(''' UIL SPELLER ''')    

    st.write(' ### ')
    col1, col2, col3, col4 = st.columns([2,6,2,2])
    col1.caption('uilspeller.app')
    col3.caption(' [Privacy Policy]()')
    col4.caption( ' [Terms of Use]() ')


    
