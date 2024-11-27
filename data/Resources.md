
def save_resources_to_file(resources):
    with open("resources.md", "w") as file:
        file.write("# Resources for AI/ML Use Cases\n\n")
        for resource in resources:
            file.write(f"### Use Case: {resource['Use Case']}\n")
            file.write(f"Dataset: [Link]({resource['Dataset']})\n\n")
