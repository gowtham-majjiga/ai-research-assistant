import streamlit as st
from app.pipeline import research

st.set_page_config(page_title="AI Research Assistant", page_icon="🔎", layout="wide")

st.title("AI Research Assistant")
st.caption("Evidence-first multi-source research with transparent retrieval and ranking.")

with st.sidebar:
    st.header("Research settings")
    max_sources = st.slider("Sources to display", 3, 12, 8)
    st.info("Public-source mode works without a paid model API.")

query = st.text_area(
    "Research question",
    placeholder="Compare retrieval-augmented generation with fine-tuning.",
    height=120,
)

if st.button("Run research", type="primary", disabled=not query.strip()):
    with st.spinner("Planning, retrieving and ranking evidence..."):
        result = research(query.strip(), max_sources=max_sources)

    if not result["sources"]:
        st.error(result["answer"])
    else:
        c1, c2, c3 = st.columns(3)
        c1.metric("Sources", len(result["sources"]))
        c2.metric("Subqueries", len(result["subqueries"]))
        c3.metric("Providers", len({s["source"] for s in result["sources"]}))

        st.subheader("Research summary")
        st.write(result["answer"])

        st.subheader("Evidence")
        for idx, source in enumerate(result["sources"], 1):
            with st.expander(f"{idx}. {source['title']} · {source['source']} · score {source['score']}"):
                st.write(source["snippet"])
                st.markdown(f"[Open source]({source['url']})")
