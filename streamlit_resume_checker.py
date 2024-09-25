import streamlit as st
import openai
import docx
import PyPDF2
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set OpenAI API Key
openai.api_key = openai_api_key

# Function to extract text from a DOCX file
def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    return "\n".join([para.text for para in doc.paragraphs])

# Function to extract text from a PDF file using PyPDF2
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

# Function to call GPT-4 to get feedback on the resume
def get_gpt_feedback(resume_text, job_description):
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

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an ATS resume analyzer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500
    )

    feedback = response.choices[0].message.content
    
    return feedback

# Streamlit App
def main():
    st.title("ATS Resume Analyzer with GPT-4o")

    st.write("""
    Upload your resume (PDF or DOCX), paste the job description, and click "Analyze Resume" to receive feedback on skill gaps, keyword optimization, and general improvements.
    """)

    # Resume file upload
    uploaded_file = st.file_uploader("Choose a resume file (PDF or DOCX)", type=["pdf", "docx"])

    # Job description input
    job_description = st.text_area("Paste the job description here")

    # Button to trigger the resume analysis
    if st.button("Analyze Resume"):
        if uploaded_file and job_description:
            # Extract resume text based on file type
            if uploaded_file.name.endswith(".docx"):
                resume_text = extract_text_from_docx(uploaded_file)
            elif uploaded_file.name.endswith(".pdf"):
                resume_text = extract_text_from_pdf(uploaded_file)
            else:
                st.error("Unsupported file format. Please upload a .pdf or .docx file.")
                return

            # Get GPT-4 feedback
            with st.spinner('Analyzing your resume...'):
                feedback = get_gpt_feedback(resume_text, job_description)
            
            # Display the feedback
            st.markdown(feedback, unsafe_allow_html=True)
        else:
            st.warning("Please upload a resume and enter a job description before analyzing.")

if __name__ == "__main__":
    main()