import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Load and encode image
image = Image.open('dp.jpeg')
buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Inject JavaScript to hide the header and footer
hide_streamlit_style = """
    <style>
    /* Hide Streamlit header and footer */
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# App styling and layout with improved mobile responsiveness
st.markdown(
    """
    <style>
    /* Main background styling */
    .main {
        background-color: #483D8B;
        color: white;
    }

    /* Circular image styling */
    .circular-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #fff;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        width: 150px; /* Set a default width */
    }

    /* Button styling */
    .animated-button {
        background-color: #00CED1;
        color: black;
        width: 100%;
        padding: 12px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.3s ease;
        margin-top: 10px;
    }
    .animated-button:hover {
        background-color: #20B2AA;
        transform: scale(1.05);
    }

    /* Contact link styling */
    .contact-link {
        color: white !important;
        font-size: 14px;
        text-decoration: underline;
        margin-top: 20px;
        display: inline-block;
    }

    /* Media queries for better responsiveness */
    @media only screen and (max-width: 768px) {
        /* Mobile view: Stack columns vertically */
        .streamlit-expanderHeader {
            flex-direction: column;
        }

        /* Reduce font size and margin for mobile */
        h1 {
            font-size: 24px;
            margin-top: 10px;
        }

        .circular-image {
            width: 120px;  /* Adjusted for smaller screens */
        }

        p {
            font-size: 14px;
            margin-top: 12px;
        }

        .animated-button {
            font-size: 14px;
            padding: 10px;
            margin-top: 8px;
        }

        .contact-link {
            font-size: 12px;
        }
    }

    @media only screen and (min-width: 769px) {
        /* Desktop view: Larger font size */
        h1 {
            font-size: 32px;
        }

        p {
            font-size: 16px;
        }

        .circular-image {
            width: 200px;
        }

        .animated-button {
            font-size: 16px;
            padding: 12px;
        }

        .contact-link {
            font-size: 14px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Conditional layout for mobile and desktop
if st.session_state.get("width", 800) < 768:
    # Mobile: stack content vertically
    col1, col2 = st.container(), st.container()
else:
    # Desktop: use columns
    col1, col2 = st.columns(2)

with col2:
    st.markdown( 
        """
        <div style="text-align: center;margin-top: 20px;">
            <h1 style="color: white;">Abhisek De</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: center;">
            <a href="https://github.com/abhisekde96" target="_blank">
                <button class="animated-button">
                    View my projects on GitHub
                </button>
            </a>
        </div>

        <div style="text-align: center;">
            <a href="https://drive.google.com/file/d/1O7Mgka5h1AAaR41c9JNpHeZ0NZsDyWqa/view?usp=sharing" target="_blank">
                <button class="animated-button">
                    View my resume
                </button>
            </a>
        </div>

        <div style="text-align: center;">
            <a href="https://www.linkedin.com/in/abhisek-de-20b966172/" target="_blank">
                <button class="animated-button">
                    Follow me on LinkedIn
                </button>
            </a>
        </div>

        <div style="text-align: center;">
            <a href="https://ieeexplore.ieee.org/document/9361221">
                <button class="animated-button">
                    View my publication
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

with col1:
    st.markdown(
        f'<img src="data:image/jpeg;base64,{img_str}" class="circular-image">',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="font-size: 14px; text-align: center;">
            Business analyst with a passion for data and a knack for building apps from scratch. 
            Turning insights into action, one dataset at a time.<br> 
            Looking forward to collaborate on exciting ideas, cheers!
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <a href="https://mail.google.com/mail/?view=cm&fs=1&to=abhisekde96@gmail.com" target="_blank" class="contact-link">
            Reach me out @
        </a>
        """,
        unsafe_allow_html=True
    )
