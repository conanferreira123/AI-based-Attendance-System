import streamlit as st
from src.components.header import header_dashboard
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.database.db import teacher_login,teacher_exists,create_teacher,check_pass,hash_pass
import time

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if 'teacher_data' in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state['teacher_login_type']=='login':
        teacher_screen_login()
    elif st.session_state['teacher_login_type']=='register':
        teacher_screen_register()

def teacher_dashboard():
    teacher_data=st.session_state.teacher_data
    st.header(f"""Welcome, {teacher_data['name']}""")
    
def login_teacher(username,password):
    if not(username or password):
        return False
    teacher=teacher_login(username,password)
    if teacher:
        st.session_state.user_role='teacher'
        st.session_state.teacher_data=teacher
        st.session_state.is_logged_in=True
        return True

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
        if st.button('Login',icon=':material/passkey:'):
            if login_teacher(teacher_username,teacher_password):
                st.toast('Successfully Logged in')
                time.sleep(1)
                st.rerun()
            else:
                st.error('Invalid Credentials')
            
    with btnc2:
        if st.button('Register Instead',icon=':material/passkey:'):
            st.session_state['teacher_login_type']='register'
            st.rerun()

def register_teacher(username,name,password,confirm_password):
    if not(username or name or password):
        return False,"All fields are required"
    elif teacher_exists(username):
        return False,"Username already exists."
    elif password != confirm_password:
        return False,"password doesnt match"
    try:
        create_teacher(username,name,password)
        return True,"Successfully created"
    except Exception as e:
        return False,str(e)

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
        if st.button('Register',icon=':material/passkey:'):
            success,message=register_teacher(teacher_username,teacher_name,teacher_password,teacher_pass_confirm)
            if success:
                st.success(message)
                time.sleep(2)
                st.session_state['teacher_login_type']="login"
                st.rerun()
            else:
                st.error(message)
                time.sleep(2)
                st.session_state['teacher_login_type']="register"
                st.rerun()
    with btnc2:
        if st.button('Login Instead',icon=':material/passkey:'):
            st.session_state['teacher_login_type']='login'
            st.rerun()
        

