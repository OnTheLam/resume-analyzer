# file_utils.py
# This module contains utility functions for handling file uploads and extracting text
# from different file formats. It currently supports PDF and DOCX files.

import streamlit as st
import docx
import PyPDF2
from io import BytesIO

@st.cache_data
def extract_text_from_docx(docx_file_content):
    """
    Extracts text from a DOCX file.

    Parameters:
    - docx_file_content: The binary content of the uploaded DOCX file.
    
    Returns:
    - The extracted text from the DOCX file as a string.
    """
    try:
        doc = docx.Document(BytesIO(docx_file_content))
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        st.error(f"Error reading DOCX file: {e}")
        return ""

@st.cache_data
def extract_text_from_pdf(pdf_file_content):
    """
    Extracts text from a PDF file.
    
    Parameters:
    - file_content: The binary content of the uploaded PDF file.
    
    Returns:
    - The extracted text from the PDF file as a string.
    """
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_file_content))
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return ""
