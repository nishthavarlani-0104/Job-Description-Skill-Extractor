import streamlit as st

from model import create_model
from parser import create_parser
from prompt import create_prompt
from main import extract_job_description


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Job Description Skill Extractor",
    page_icon="💼",
    layout="wide"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* App background */
    .stApp {
        background: linear-gradient(
            135deg,
            #f8f5ff 0%,
            #f1e8ff 50%,
            #faf7ff 100%
        );
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #6d28d9;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        font-size: 17px;
        color: #7e22ce;
        margin-bottom: 20px;
    }

    /* Text area */
    .stTextArea textarea {
        border: 2px solid #c4b5fd !important;
        border-radius: 14px !important;
        background-color: white !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #7c3aed, #9333ea);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        padding: 10px 24px;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #6d28d9, #7e22ce);
        color: white;
    }

    /* Watermark */
    .watermark {
        position: fixed;
        bottom: 15px;
        right: 25px;
        color: rgba(109, 40, 217, 0.45);
        font-size: 14px;
        font-weight: 600;
        font-style: italic;
        z-index: 9999;
        pointer-events: none;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# WATERMARK
# ---------------------------------------------------------

st.markdown(
    """
    <div class="watermark">
        Developed by Nishtha Varlani
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="main-title">
        💼 Job Description Skill Extractor
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Paste a job description below to extract skills, experience, and education.
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# JOB DESCRIPTION INPUT
# ---------------------------------------------------------

job_description = st.text_area(
    "Job Description",
    placeholder="Paste the job description here...",
    height=250,
    key="job_description"
)


# ---------------------------------------------------------
# BUTTONS
# ---------------------------------------------------------

button_col1, button_col2 = st.columns(2)

with button_col1:

    if st.button("Extract Information", type="primary"):

        if not job_description.strip():

            st.warning("Please enter a job description.")

        else:

            with st.spinner("Extracting information..."):

                try:

                    result = extract_job_description(job_description)

                    st.session_state.result = result

                    st.success("Information extracted successfully!")

                except Exception as e:

                    st.error(f"Something went wrong: {e}")


with button_col2:

    if st.button("🗑️ Clear"):

        if "job_description" in st.session_state:
            del st.session_state["job_description"]

        if "result" in st.session_state:
            del st.session_state["result"]

        st.rerun()


# ---------------------------------------------------------
# RESULTS
# ---------------------------------------------------------

if "result" in st.session_state:

    result = st.session_state.result

    result_data = result.model_dump()

    st.divider()

    st.subheader("✨ Extracted Information")

    col1, col2, col3 = st.columns(3)


    # -----------------------------------------------------
    # SKILLS
    # -----------------------------------------------------

    with col1:

        st.subheader("🛠️ Skills")

        skills = result_data.get("skills", [])

        if skills:
            st.write(skills)
        else:
            st.write("Not available")


    # -----------------------------------------------------
    # EXPERIENCE
    # -----------------------------------------------------

    with col2:

        st.subheader("💼 Experience")

        experience = result_data.get(
            "experience",
            "Not available"
        )

        st.write(experience)


    # -----------------------------------------------------
    # EDUCATION
    # -----------------------------------------------------

    with col3:

        st.subheader("🎓 Education")

        education = result_data.get(
            "education",
            "Not available"
        )

        st.write(education)