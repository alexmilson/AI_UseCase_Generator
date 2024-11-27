from transformers import pipeline
import requests
from bs4 import BeautifulSoup

def research_agent(company_name):
    search_query = f"{company_name} industry and operations"
    response = requests.get(f"https://www.google.com/search?q={search_query}")
    soup = BeautifulSoup(response.text, "html.parser")
    # Extract basic information (modify as needed)
    descriptions = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
    details = " ".join([desc.text for desc in descriptions[:3]])
    
    classifier = pipeline("zero-shot-classification", model="distilbert-base-uncased")
    industries = ["Automotive", "Healthcare", "Finance", "Retail", "Manufacturing", "Technology"]
    classification = classifier(details, industries)
    return classification["labels"][0], details
