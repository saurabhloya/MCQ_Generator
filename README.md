# MCQ_Generator

This repository contains a web application that harnesses OpenAI's Language Model, Langchain, and Streamlit to automate the generation of multiple-choice questions (MCQs). 

## Features

- **Automated MCQ Generation**: Uses OpenAI's language model to create multiple-choice questions based on provided content.
- **Interactive UI**: Built with Streamlit for a simple and user-friendly interface.
- **Customizable Options**: Users can customize the number of questions, difficulty level, and more.

## Installation

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/saurabhloya/MCQ_Generator.git
   cd MCQ_Generator
   ```

2. **Create a Virtual Environment**:
   ```bash
   conda create -p venv python=3.9 -y
   conda activate venv
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add OpenAI API Key**:
   - Generate an OpenAI API Key from the OpenAI website.
   - Create a `.env` file in the root directory of the project and add your API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

5. **Run the Application**:
   ```bash
   streamlit run StreamlitAPP.py
   ```

6. **Access the Application**:
   - Open your web browser and go to `http://localhost:8501`.
