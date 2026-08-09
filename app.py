import os
import requests
import streamlit as st
from app.pipeline import research

st.set_page_config(page_title="AI Research Assistant", page_icon="🔎", layout="wide")
st.title("AI Research Assistant")
st.caption("Multi-source retrieval with evidence-first research summaries")

query = st.text_area("Research question", placeholder="Compare retrieval-augmented generation with fine-tuning.")

if st.button("Research", type="primary", disabled=not query.strip()):
    with st.spinner("Searching sources and assembling evidence..."):
        result = research(query.strip())
    st.subheader("Answer")
    st.write(result["answer"])
    st.subheader("Sources")
    for source in result["sources"]:
        st.markdown(f"- [{source['title']}]({source['url']}) — {source['source']}")
