# openai_utils.py
# This module contains utility functions for interacting with the OpenAI API.
# It handles generating feedback for the resume analysis and generating 
# assistant responses for the chatbot.

import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@st.cache_data(show_spinner=False)
def get_gpt_feedback(resume_text, job_description):
    """
    Sends the resume text and job description to the OpenAI GPT API for feedback.
    The assistant provides optimization suggestions based on the job description and resume.
    
    Parameters:
    - resume_text: The extracted text of the uploaded resume (string).
    - job_description: The job description provided by the user (string).
    
    Returns:
    - Feedback from GPT-4, including recommendations for optimizing the resume (string).
    """


    prompt = f"""
    You are ResumeChecker, an expert in ATS optimization. Analyze the following resume and provide optimization suggestions:

    1. Identify keywords from the job description that should be included in the resume.
    2. Suggest reformatting or restructuring to improve ATS readability.
    3. Recommend changes to improve keyword density without keyword stuffing.
    4. Provide 3-5 bullet points on how to tailor this resume for the specific job description.
    5. Give an ATS compatibility score out of 100 and explain how to improve it.

    Resume text: {resume_text}
    Job description: {job_description}
    """

    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an ATS resume analyzer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500
        )

        feedback = response.choices[0].message.content
        return feedback
    except openai.OpenAIError as e:
        st.error(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None

def generate_assistant_response(messages):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            stream=True,
            max_tokens=150
        )
        return response
    except openai.OpenAIError as e:
        st.error(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None
