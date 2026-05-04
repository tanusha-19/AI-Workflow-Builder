import streamlit as st

def apply_custom_design():
    st.markdown("""
        <style>
        /* Global Background & Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #0b0d17 0%, #1a1c2c 100%);
            font-family: 'Inter', sans-serif;
            color: #ffffff;
        }

        /* Hero Section Styling */
        .hero-title {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(90deg, #a855f7, #3b82f6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }

        /* Hide Default Elements */
        button[title="Reset"], button[title="Zoom In"], button[title="Zoom Out"] {
            display: none !important;
        }
        #MainMenu, footer, header {visibility: hidden;}

        /* Card Styling for Input */
        div[data-testid="stVerticalBlock"] > div:has(div.stTextArea) {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 24px;
            backdrop-filter: blur(20px);
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
        }

        /* Neon Primary Button */
        .stButton > button {
            background: #6366f1;
            border: none;
            color: white;
            padding: 15px 30px;
            border-radius: 12px;
            font-weight: 600;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .stButton > button:hover {
            background: #4f46e5;
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.6);
            transform: translateY(-2px);
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: rgba(15, 17, 26, 0.8);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)