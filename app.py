# app.py
import streamlit as st
from agents.research_agent import get_industry_info
from agents.usecase_agent import generate_use_cases
from agents.resource_agent import fetch_resources

# Streamlit UI
st.title("AI Use Case Generator")
company_name = st.text_input("Enter Company Name")

if company_name:
    st.write("Fetching industry information...")
    industry_info = get_industry_info(company_name)
    st.write(f"Industry: {industry_info['industry']}")
    st.write(f"Details: {industry_info['details']}")
    
    st.write("Generating AI/ML use cases...")
    use_cases = generate_use_cases(industry_info['industry'])
    st.write(use_cases)
    
    st.write("Fetching resources...")
    resources = fetch_resources(use_cases)
    st.write(resources)
