import streamlit as st
import langchain_helper

st.title("Restaurant name generator")

cuisine = st.sidebar.selectbox("Cuisine",("Indian","Mexican","Italian","Chinese","American","Arabic"))


if cuisine:
    response = langchain_helper.Restaurant_name_generator(cuisine)
    
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for items in menu_items:
        st.write("-",items) 
