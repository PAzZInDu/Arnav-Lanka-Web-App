import streamlit as st
import authlib


IMAGE_ADDRESS = "https://cdn.scope.digital/Images/Articles/kolon-bagirsak-kanseri-belirtileri-ve-tedavisi-5628892.jpg?tr=w-630,h-420"

if not st.user.is_logged_in:
    st.title("Human Colorectal Cancer Prediction - Google Login App")
    st.image(IMAGE_ADDRESS)
    if st.sidebar.button("Log in with Google", type="primary", icon=":material/login:"):
        st.login()
        

else:
    st.success('Please visit the App')
    #st.html(f"Hello, <span style='color: orange; font-weight: bold;'>{st.experimental_user.name}</span>!")
    if st.sidebar.button("Log out", type="secondary", icon=":material/logout:"):
        st.logout()