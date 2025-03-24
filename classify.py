import os
import pandas as pd
from processor_regex import classify_with_regex
from processor_bert import classify_with_bert
from processor_llm import classify_with_llm

# Function to classify logs
def classify(logs):
    labels = []
    for source, log_msg in logs:
        label = classify_log(source, log_msg)
        labels.append(label)
    return labels

# Function to classify a single log message
def classify_log(source, log_msg):
    if source == "LegacyCRM":
        label = classify_with_llm(log_msg)
    else:
        label = classify_with_regex(log_msg)
        if not label:
            label = classify_with_bert(log_msg)
    return label

# Function to classify logs from CSV
def classify_csv(input_file):
    # Ensure the file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"File not found: {input_file}")

    # Read the CSV file
    df = pd.read_csv(input_file)

    # Perform classification
    df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

    # Save the modified file
    output_file = "output.csv"
    df.to_csv(output_file, index=False)

    print(f"Classification completed. Output saved as: {output_file}")
    return output_file

# Run classification on test.csv
if __name__ == '__main__':
    test_file = "Resources/test.csv"  # Corrected path
    if not os.path.exists(test_file):
        print(f"Error: The file '{test_file}' does not exist.")
        print("Current Directory:", os.getcwd())
        print("Available files in 'Resources':", os.listdir("Resources") if os.path.exists("Resources") else "Folder not found")
    else:
        classify_csv(test_file)



