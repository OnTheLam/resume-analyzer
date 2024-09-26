# layout_utils.py

import streamlit as st

def detect_device():
    """
    Injects JavaScript to detect the device screen width and stores the width in session state.
    This function injects JavaScript directly into the Streamlit frontend to dynamically detect 
    the screen width when the page is loaded.
    """
    # Inject JavaScript to detect screen width and set it in session_state
    st.markdown(
        """
        <script>
        const screen_width = window.innerWidth;
        window.streamlitAPI.setComponentValue(screen_width);
        </script>
        """,
        unsafe_allow_html=True
    )

def get_layout():
    """
    Returns the layout type based on the detected screen width.
    If the screen width is less than 768px, it will return a value of 1 (mobile/tablet layout).
    If the screen width is greater than or equal to 768px, it will return a value of 2 (desktop layout).
    
    Returns:
    - 1 for mobile/tablet (1 column layout).
    - 2 for desktop (2 columns layout).
    """
    screen_width = st.session_state.get("screen_width", 768)  # Default to 768px if width is not yet available

    if screen_width < 768:
        return 1  # Mobile/Tablet (1 column layout)
    else:
        return 2  # Desktop (2 columns layout)
