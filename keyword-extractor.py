import streamlit as st
from bs4 import BeautifulSoup
import requests

st.markdown("<h1>Get Youtube Keywords</h1>",unsafe_allow_html=True)
url=st.text_input("Enter url of youtube video")
if url:
    page=requests.get(url)
    #print(page.status_code)
    soup=BeautifulSoup(page.content,'lxml') #lxml is parser
    meta_tag=soup.select("meta[name='keywords']")
    keyword=meta_tag[0]["content"]
    
    title=soup.find("title")
    st.title("Title")
    st.markdown(f"<h5>{title.text}</h5>",unsafe_allow_html=True)
    st.title("Tags")
    st.markdown(f"<h5>{keyword}</h5>",unsafe_allow_html=True)
