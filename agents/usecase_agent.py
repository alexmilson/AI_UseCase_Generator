# agents/usecase_agent.py
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("openai-community/openai-gpt")
model = AutoModelForCausalLM.from_pretrained("openai-community/openai-gpt")

def generate_use_cases(prompt: str, max_length: int = 100):
    """
    Generate use cases or text based on the given prompt using the GPT model.
    
    Args:
        prompt (str): The input text to generate use cases from.
        max_length (int): Maximum length of the generated output.
    
    Returns:
        str: The generated text.
    """
    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Generate the output text
    outputs = model.generate(inputs['input_ids'], max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2)
    
    # Decode the generated text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return generated_text
