# resume_analyzer.py
# This module handles the resume analysis functionality. It includes functions 
# for uploading and extracting the text from resumes, sending the resume for GPT analysis, 
# and displaying the feedback from the analysis.

import streamlit as st
from file_utils import extract_text_from_docx, extract_text_from_pdf
from openai_utils import get_gpt_feedback

def handle_resume_analysis():
    """
    Handles the entire process of uploading a resume, inputting a job description,
    and triggering the analysis.
    """
    
    # Only show file uploader and job description input if the analysis isn't complete
    if not st.session_state.get("analysis_complete", False):
        st.subheader("Upload Resume & Job Description")
        
        # File uploader for the resume
        uploaded_file = st.file_uploader("Drop or Select Resume File (PDF or DOCX)", type=["pdf", "docx"])
        
        # Text area for the job description
        job_description = st.text_area("Paste the job description here")

        # Trigger resume analysis when the button is pressed
        if st.button("Analyze Resume"):
            # Handle file upload and extraction
            st.session_state.resume_text = handle_file_upload(uploaded_file)
            st.session_state.job_description = job_description

            # Perform analysis if both resume and job description are provided
            if st.session_state.resume_text and st.session_state.job_description:
                feedback = analyze_resume(st.session_state.resume_text, st.session_state.job_description)
                
                if feedback:
                    st.session_state.analysis_feedback = feedback
                    st.session_state.analysis_complete = True
                else:
                    st.error("Analysis failed. Please try again.")
            else:
                st.error("Please upload both a resume and job description.")

def handle_file_upload(uploaded_file):
    """
    Handles file uploads and extracts the text from the uploaded resume.
    Supports both .pdf and .docx formats.
    
    Parameters:
    - uploaded_file: The file object uploaded by the user.
    
    Returns:
    - The extracted text from the resume if the file type is supported, otherwise None.
    """
    if not uploaded_file:
        st.error("Please upload a resume file.")
        return None
    
    try:
        file_content = uploaded_file.read()
        # Extract resume text based on file type
        if uploaded_file.name.endswith(".docx"):
            return extract_text_from_docx(file_content)
        elif uploaded_file.name.endswith(".pdf"):
            return extract_text_from_pdf(file_content)
        else:
            st.error("Unsupported file format. Please upload a .pdf or .docx file.")
            return None
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return None

def analyze_resume(resume_text, job_description):
    """
    Sends the resume text and job description to the GPT API for feedback and analysis.
    
    Parameters:
    - resume_text: The text extracted from the uploaded resume.
    - job_description: The job description provided by the user.
    
    Returns:
    - Feedback from the GPT API on the resume's compatibility with the job description, or None if it fails.
    """
    if not resume_text or not job_description:
        st.error("Both resume and job description are required.")
        return None

    with st.spinner("Analyzing your resume..."):
        feedback = get_gpt_feedback(resume_text, job_description)
        if feedback:
            st.session_state.analysis_complete = True
            return feedback
        else:
            st.error("Failed to retrieve feedback.")
            return None

def display_analysis_feedback():
    """
    Displays the feedback from the resume analysis if the analysis has been completed.
    """
    if st.session_state.analysis_complete and st.session_state.analysis_feedback:
        with st.expander(":deciduous_tree: **Resume Analysis**", expanded=True):
            st.write(st.session_state.analysis_feedback)
