import streamlit as st
from src.components.header import header_dashboard
from src.ui.base_layout import style_background_dashboard,style_base_layout

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if 'teacher_login_type' not in st.session_state or st.session_state['teacher_login_type']=='login':
        teacher_screen_login()
      
    elif st.session_state['teacher_login_type']=='register':
        teacher_screen_register()
       
    
def teacher_screen_login():
    col1,col2=st.columns(2,vertical_alignment='center',gap='large')
    with col1:
        header_dashboard()
        
    with col2:
        if st.button("Go back to Home",type='secondary',key='loginbackbtn'):
            st.session_state['login_type']=None
            st.rerun()
            
    st.header('Login using password')
    teacher_username=st.text_input("enter username",placeholder='ananya roy')
    teacher_password=st.text_input('Enter password',placeholder='password')
    st.divider()
    
    btnc1,btnc2=st.columns(2)
    
    with btnc1:
        st.button('Login',icon=':material/passkey:')
            
    with btnc2:
        if st.button('Register Instead',icon=':material/passkey:'):
            st.session_state['teacher_login_type']='register'
            st.rerun()
   
def teacher_screen_register():
    col1,col2=st.columns(2,vertical_alignment='center',gap='large')
    with col1:
        header_dashboard()
        
    with col2:
        if st.button("Go back to Home",type='secondary',key='loginbackbtn'):
            st.session_state['login_type']=None
            st.rerun()
    
    st.header('Register')
    teacher_name=st.text_input('enter name',placeholder='ananya pandey')
    teacher_username=st.text_input("enter username",placeholder='ananyapanda123')
    teacher_password=st.text_input('enter password',placeholder='password')
    teacher_pass_confirm=st.text_input('confirm password',placeholder='password')
    st.divider()
    
    btnc1,btnc2=st.columns(2)
    
    with btnc1:
        st.button('Register',icon=':material/passkey:')
    with btnc2:
        if st.button('Login Instead',icon=':material/passkey:'):
            st.session_state['teacher_login_type']='login'
            st.rerun()
        

