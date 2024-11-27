from transformers import pipeline

def use_case_agent(industry):
    generator = pipeline("text-generation", model="gpt2")
    prompt = f"Generate AI/ML use cases for the {industry} industry:"
    use_cases = generator(prompt, max_length=100, num_return_sequences=3)
    return [case['generated_text'] for case in use_cases]
