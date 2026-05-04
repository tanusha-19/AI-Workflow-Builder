import streamlit as st
from streamlit_mermaid import st_mermaid
from style import apply_custom_design

# Initialize visual styles
apply_custom_design()

# --- HERO SECTION ---
st.markdown('<h1 class="hero-title">Smart Workflow Builder</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 1.2rem; color: #94a3b8; margin-bottom: 2rem;">Ship working logic visually in seconds. Built for scale.</p>', unsafe_allow_html=True)

# --- CONTROLS ---
col_input, col_settings = st.columns([2, 1])

with col_settings:
    st.markdown("### Configuration")
    orientation = st.selectbox("Flow Orientation", ["Horizontal", "Vertical"])
    dir_code = "LR" if orientation == "Horizontal" else "TD"
    
with col_input:
    user_input = st.text_area(
        "Enter your workflow logic:", 
        placeholder="Fetch data, If valid / Check values, Save to record, Notify team",
        height=150
    )
    generate_btn = st.button("Generate Workflow")

# --- LOGIC ENGINE ---
def get_smart_style(text):
    text = text.lower()
    if any(k in text for k in ["if", "check", "verify", "valid"]):
        return "{", "}", "#f59e0b" # Orange Diamond
    if any(k in text for k in ["save", "db", "database", "record"]):
        return "(", ")", "#06b6d4" # Cyan Rounded
    if any(k in text for k in ["send", "notify", "email", "alert"]):
        return "([", "])", "#6366f1" # Indigo Stadium
    return "[", "]", "#10b981" # Green Rectangle

# --- OUTPUT ---
if generate_btn:
    if user_input:
        steps = [s.strip() for s in user_input.split(",") if s.strip()]
        chart_code = f"graph {dir_code}\n"
        
        for i, step in enumerate(steps):
            open_s, close_s, color = get_smart_style(step)
            clean_text = step.replace("/", "<br/>")
            chart_code += f"  node{i}{open_s}\"{clean_text}\"{close_s}\n"
            
            if i < len(steps) - 1:
                chart_code += f"  node{i} --> node{i+1}\n"
            
            chart_code += f"  style node{i} fill:{color}33,stroke:{color},stroke-width:2px,color:#fff\n"

        st.markdown('<div style="margin-top: 3rem;"></div>', unsafe_allow_html=True)
        st.subheader("📊 Live Canvas")
        st_mermaid(chart_code, height=500)
    else:
        st.info("The editor is empty. Start by typing your logic above.")