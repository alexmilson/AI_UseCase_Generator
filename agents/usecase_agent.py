def generate_use_cases(industry):
    use_cases = [
        f"1. Predictive Maintenance: Reduce equipment downtime in {industry} using ML algorithms.",
        "2. Customer Personalization: Utilize AI to enhance customer experience through targeted marketing.",
    ]
    
    with open('data/Use_Cases.md', 'w') as file:
        file.write("\n".join(use_cases))
    return use_cases
