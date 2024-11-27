import streamlit as st
from agents.research_agent import get_industry_info
from agents.usecase_agent import generate_use_cases
from agents.resource_agent import fetch_resources

st.title("AI Use Case Generator")

# Input
company_name = st.text_input("Enter Company Name")

if st.button("Generate Insights"):
    industry = get_industry_info(company_name)
    st.write(f"**Industry Identified:** {industry}")

    use_cases = generate_use_cases(industry)
    st.markdown("### Use Cases")
    st.markdown("\n".join(use_cases))

    resources = fetch_resources(use_cases)
    st.markdown("### Resources")
    st.markdown("\n".join(resources))
