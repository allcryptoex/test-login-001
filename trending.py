import streamlit as st
from firebase_admin import auth

def app():
    #st.header(' MWANACHUO PLATFORM!! ')
    
    header1, header2 = st.columns([0.75,3])
    with header1:
        container1 = st.container(border=True)   
        container1.image('logo.png', width=100)


    st.header(' :green[Getting Started!!]')


    
