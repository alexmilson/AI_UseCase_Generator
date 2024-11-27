# app.py
import streamlit as st
from agents.research_agent import get_industry_info
from agents.usecase_agent import generate_use_cases
from agents.resource_agent import fetch_resources

# Streamlit UI setup
st.set_page_config(page_title="AI Use Case Generator", page_icon=":guardsman:", layout="wide")

st.title("AI Use Case Generator")

# User input
prompt = st.text_area("Enter the prompt for generation:", "AI in Healthcare")

# Option to select type of generation
generation_type = st.radio("Select Generation Type:", ("Industry Info", "Use Cases", "Resources"))

# Generate button
if st.button("Generate"):
    if prompt:
        if generation_type == "Industry Info":
            generated_text = get_industry_info(prompt)
            st.write("Generated Industry Info:")
            st.write(generated_text)
        elif generation_type == "Use Cases":
            generated_text = generate_use_cases(prompt)
            st.write("Generated Use Cases:")
            st.write(generated_text)
        elif generation_type == "Resources":
            generated_text = fetch_resources(prompt)
            st.write("Fetched Resources:")
            st.write(generated_text)
    else:
        st.error("Please enter a prompt to generate content.")
