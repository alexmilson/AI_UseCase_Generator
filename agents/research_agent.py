# research_agent.py
from transformers import pipeline
import requests
from bs4 import BeautifulSoup

def get_industry_info(company_name):
    """
    Fetches the industry and basic information about a company.
    
    Args:
        company_name (str): The name of the company to research.
    
    Returns:
        dict: A dictionary containing the industry and other details.
    """
    search_query = f"{company_name} industry and operations"
    response = requests.get(f"https://www.google.com/search?q={search_query}")
    soup = BeautifulSoup(response.text, "html.parser")
    # Extract basic information
    descriptions = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
    details = " ".join([desc.text for desc in descriptions[:3]])
    
    # Use zero-shot classification to determine the industry
    classifier = pipeline("zero-shot-classification", model="distilbert-base-uncased")
    industries = ["Automotive", "Healthcare", "Finance", "Retail", "Manufacturing", "Technology"]
    classification = classifier(details, industries)
    
    return {
        "industry": classification["labels"][0],
        "details": details
    }
