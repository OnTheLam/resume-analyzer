# css_utils.py

import streamlit as st

def load_css(css_file_path):
    """
    Loads custom CSS from a file and applies it to the Streamlit app.

    Parameters:
    - css_file_path: Path to the CSS file.
    """
    with open(css_file_path) as f:
        css_content = f.read()
        st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
