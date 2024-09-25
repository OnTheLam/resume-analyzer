# resume-analyzer
ATS resume checker using streamlit and OpenAI NLP.

## Overview

The **Resume Analyzer** is a web application built with **Streamlit** that allows users to upload their resumes (in PDF or DOCX format) and paste a job description to receive optimization feedback tailored for Applicant Tracking Systems (ATS). The app utilizes OpenAI's GPT-4 model to provide feedback on skill gaps, keyword optimization, ATS compatibility score, and general improvements to tailor resumes to specific job descriptions.

## Features

- **Resume Parsing**: Supports both PDF and DOCX formats for resume uploads.
- **Job Description Input**: Allows users to paste the job description for personalized feedback.
- **ATS Feedback**: Provides suggestions to improve ATS readability, keyword density, and formatting.
- **ATS Compatibility Score**: Offers an ATS compatibility score out of 100 with recommendations for improvement.
- **User-Friendly Interface**: Built with Streamlit, offering a simple and interactive experience.

## Requirements

- Python 3.7 or higher
- OpenAI API Key
- OpenAI API Key

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/OnTheLam/resume-analyzer.git
   cd resume-analyzer
   ```
2. **Set up a virtual environment (optional but recommended):**
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. **Install the required Python packages:**
    ```
    pip install -r requirements.txt
    ```
4. **Create a .env file in the project root directory to store your OpenAI API key:**
    ```
    touch .env   # On Windows, use echo.> .env
    ```
5. **Inside the .env file, add your OpenAI API key like this:**
    ```
    OPENAI_API_KEY="your-openai-api-key-here"
    ```
6. **Run the Streamlit app**
    ```
    streamlit run app.py
    ```
