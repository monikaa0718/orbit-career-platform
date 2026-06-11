import streamlit as st

st.set_page_config(
    page_title="Orbit",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Orbit")
st.subheader("Open Source Resume Analyzer & Career Guidance Platform")

st.markdown("""
Welcome to Orbit!

Features:
- Resume Analysis
- ATS Score
- Skill Gap Analysis
- Career Recommendations
- Learning Roadmaps
""")

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:
    st.success("Resume uploaded successfully!")