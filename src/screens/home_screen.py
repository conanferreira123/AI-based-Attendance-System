import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_background_dashboard,style_background_home,style_base_layout

def home_screen():
    header_home()
    style_background_home()
    style_base_layout()
    
    st.header("home screen")
    
    col1,col2=st.columns(2)
    
    with col1:
        if st.button('Student login'):
            st.session_state['login_type']='student'
            st.rerun()
        
    with col2:
        if st.button('Teacher login'):
            st.session_state['login_type']='teacher'
            st.rerun()

