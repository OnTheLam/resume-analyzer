# chatbot.py
# This module manages the chatbot functionality, including user interaction and 
# generating assistant responses. It also integrates the resume and job description context 
# into the chatbot's conversation.

import time
import streamlit as st
from openai_utils import generate_assistant_response
from chat_utils import append_user_message, append_assistant_message, display_chat_messages

def handle_chatbot_interaction():
    """
    Handles the chatbot interaction, allowing the user to send messages to the GPT assistant.
    It integrates the resume text and job description into the chatbot's context for more 
    personalized and relevant responses.
    """
    st.subheader(":material/chat: Resume Assistant")
    
    # Ensure session state for messages is initialized
    if "messages" not in st.session_state:
        st.session_state.messages = []

    display_chat_messages()
    
    if prompt := st.chat_input("Ask about your resume analysis, career advice, or ATS optimization."):
        append_user_message(prompt)
        
        messages = st.session_state.messages

        # Prepare system message (context) for the assistant, but don't store it
        system_message = {
            "role": "system",
            "content": f"""You are a helpful assistant for resume optimization.
                The user has uploaded the following resume:
                {st.session_state.resume_text}
                
                The user also provided the following job description:
                {st.session_state.job_description}

                This was the resume analysis that you previously gave the user:
                {st.session_state.analysis_feedback}

                Provide answers based on this information.
                """
            }    
        
        # Generate assistant's response with system message included in API call
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
                
            # Combine system message with conversation history for API call
            api_messages = [system_message] + messages
            
            retries = 3
            while retries > 0:
                try:
                    #Stream assistant response
                    with st.spinner("Assistant is responding..."):
                        response_stream = generate_assistant_response(api_messages)

                        if response_stream:
                            for chunk in response_stream:
                                # Safely access the 'content' attribute and ensure it's a string
                                chunk_content = getattr(chunk.choices[0].delta, 'content', '') or ''
                                full_response += chunk_content
                                message_placeholder.markdown(full_response + "▌")
                            message_placeholder.markdown(full_response)
                        else:
                            st.error("Failed to get assistant response.")
                    break
                except Exception as e:
                    retries -= 1
                    if retries == 0:
                        st.error(f"Connection failed after multiple attempts: {e}")
                    else:
                        st.warning(f"Connection error, retrying... ({3 - retries}/3)")
                        time.sleep(2)  # Wait a little before retrying

        # Append assistant's response to the conversation history directly
            append_assistant_message(full_response)
