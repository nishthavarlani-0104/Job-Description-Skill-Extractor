import streamlit as st

from model import create_model
from parser import create_parser
from prompt import create_prompt
from main import extract_job_description

st.set_page_config(page_title="Job Description Skill Extractor",page_icon="👜",layout="wide")
st.title("👜 :green[Job Description Skill Extractor]")
st.subheader(":red[Paste a job description below to extract skills, experience, and education.]")

st.divider()

job_description=st.text_area("Job Description",placeholder="Paste the job description here...",height=250)

if st.button("Extract Information",type="primary"):
    if not job_description.strip():
        st.warning("please enter a job description.")

    else:
        with st.spinner("Extracting information..."):
            try:
                result=extract_job_description(job_description)
                st.success("Information extracted successfully!")
                st.subheader("Extracted Information")
                result_data=result.model_dump()
                st.json(result_data)
            except Exception as e:
                st.error(f"Something went wrong: {e}")      