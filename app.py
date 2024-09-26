# app.py

import streamlit as st


# Import functions from the modules
from state_manager import initialize_session_state
from resume_analyzer import handle_resume_analysis, display_analysis_feedback
from chatbot import handle_chatbot_interaction
from css_utils import load_css
from layout_utils import detect_device, get_layout

def main():
    """
    The main function of the Streamlit app. It orchestrates the resume analysis and chatbot functionalities,
    allowing users to upload resumes, receive feedback, and interact with a GPT-powered assistant.
    """
    load_css("style.css")
    detect_device()
    layout_type = get_layout()
    

    st.title("Duncan's Resume Analyzer")

    # Initialize session state
    initialize_session_state()

    # Desktop layout (2 columns)
    if layout_type == 2:
        # Create two columns
        col1, col2 = st.columns([1, 1])  # Define equal width columns

        # Column 1: Resume Analyzer
        with col1:
            handle_resume_analysis()
            display_analysis_feedback()


        # Column 2: Chatbot Interaction
        with col2:
            handle_chatbot_interaction()
    else:
        handle_resume_analysis()
        display_analysis_feedback()
        handle_chatbot_interaction()

if __name__ == "__main__":
    main()