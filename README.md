# Log Classification with Hybrid Classification Framework

## Project Overview
This project is an advanced log classification system that utilizes a hybrid classification framework. It integrates rule-based, machine learning, and large language model (LLM) approaches to classify log messages effectively.

## Features
- **Hybrid Classification Framework**: Combines regex-based, BERT-based, and LLM-based classification techniques.
- **CSV-based Classification**: Reads logs from a CSV file and assigns categories to each log message.
- **REST API Support**: Provides a FastAPI-based endpoint for classifying logs dynamically.
- **Pre-trained Model Integration**: Uses a pre-trained BERT model for classification.
- **Regex-Based Classification**: Fast, rule-based classification for structured log messages.
- **LLM-Powered Classification**: Uses deep learning models for complex log message interpretation.

## Project Structure
```
├── classify.py             # Main classification logic
├── processor_bert.py       # BERT-based classification
├── processor_llm.py        # LLM-based classification
├── processor_regex.py      # Regex-based classification
├── server.py               # FastAPI server for log classification
├── log_classification.ipynb # Jupyter notebook for model evaluation
├── requirements.txt        # Dependencies for the project
├── README.md               # Project documentation
```

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/Mfahadrafiq/Log-Classification.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Log-Classification-with-Hybrid-Classification-Framework
   ```
3. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### **Classify Logs from CSV**
Run the following command to classify logs from a CSV file:
```sh
python classify.py
```
Make sure your CSV file is placed in the `Resources/` folder and has the required columns (`source`, `log_message`).

### **Run FastAPI Server**
Start the FastAPI server to classify logs via API:
```sh
uvicorn server:app --reload
```
Use the `/classify/` endpoint to upload a CSV file and receive classified log messages.

## Example API Usage
Send a POST request with a CSV file to classify logs:
```sh
curl -X POST "http://127.0.0.1:8000/classify/" -F "file=@test.csv"
```

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.


