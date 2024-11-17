"""
Search interface
"""

import streamlit as st
from retriever import init_index, query_index

st.title("RAG")


@st.cache_resource
def init():
    init_index()

init()


def format_text(text, prefix):
    text = [i.strip() for i in text.split("\n")]
    text = str(prefix) + ". ... " + " ".join(text) + " ..."
    return text



prompt = st.chat_input("Query goes here ...")
if prompt:
    st.write(f"User: {prompt}")
    resp = query_index(prompt, k=5)
    for idx, rec in enumerate(resp):
        st.markdown(format_text(rec[0].page_content, idx+1))
 

