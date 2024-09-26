# state_manager.py
# This module is responsible for initializing the session state variables
# used throughout the app. These variables are stored in Streamlit's session state 
# and control the state of resume analysis, feedback, messages, and chat initialization.

import streamlit as st

def initialize_session_state():
    """
    Initializes all the necessary session state variables if they do not already exist.
    These variables include:
    - analysis_complete: Whether the resume analysis is complete.
    - analysis_feedback: Stores the feedback from the GPT resume analysis.
    - messages: Stores the history of messages in the chatbot conversation.
    - chat_initialized: Tracks if the chatbot has been initialized.
    - resume_text: Stores the extracted resume text for reference in the chatbot.
    - job_description: Stores the job description provided by the user.
    """
    if "analysis_complete" not in st.session_state:
        st.session_state.analysis_complete = False
    if "analysis_feedback" not in st.session_state:
        st.session_state.analysis_feedback = None
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "chat_initialized" not in st.session_state:
        st.session_state.chat_initialized = False
    if "resume_text" not in st.session_state:
        st.session_state.resume_text = None
    if "job_description" not in st.session_state:
        st.session_state.job_description = None