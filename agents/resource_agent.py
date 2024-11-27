from sentence_transformers import SentenceTransformer, util
import pandas as pd

def resource_agent(use_cases):
    # Sample dataset metadata (replace with real dataset links)
    datasets = pd.DataFrame({
        "Name": ["Machine Sensor Data", "Customer Feedback", "Supply Chain Logs"],
        "Link": ["https://kaggle.com/sensor-data", "https://huggingface.co/feedback-dataset", "https://github.com/supply-chain"],
        "Description": [
            "Sensor data for predicting machine failures",
            "Customer feedback analysis for sentiment prediction",
            "Logs of supply chain operations for efficiency optimization"
        ]
    })
    
    model = SentenceTransformer('all-MiniLM-L6-v2')
    case_embeddings = model.encode(use_cases)
    dataset_embeddings = model.encode(datasets["Description"])
    
    results = []
    for i, case_emb in enumerate(case_embeddings):
        similarities = util.pytorch_cos_sim(case_emb, dataset_embeddings)
        top_idx = similarities.argmax().item()
        results.append({"Use Case": use_cases[i], "Dataset": datasets.iloc[top_idx]["Link"]})
    return results
