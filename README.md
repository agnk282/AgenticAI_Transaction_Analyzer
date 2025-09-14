# AgenticAI Transaction Analyzer

## Overview
AgenticAI Transaction Analyzer is a Python application designed to analyze and visualize Visa transaction data using AI-powered insights. It leverages OpenAI and Google Generative AI APIs for advanced analytics and provides an interactive user interface via Streamlit.

## Features
- Analyze Visa transaction data from a local SQLite database (`visa_transactions.db`).
- AI-powered insights and analytics using OpenAI and Google Generative AI.
- Interactive dashboard built with Streamlit.
- Modular codebase for easy extension and customization.

## Requirements
- Python 3.8+
- See `requirements.txt` for all dependencies.

## Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone https://github.com/agnk282/AgenticAI_Transaction_Analyzer.git
   cd AgenticAI_Transaction_Analyzer
   ```
2. **Create and activate a virtual environment (recommended):**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   - Create a `.env` file in the project root with your API keys and configuration. Example:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     GOOGLE_API_KEY=your_google_api_key
     ```
5. **Run the application:**
   
## File Structure
- `app_visa_transactions.py` — Streamlit app entry point
- `main.py` — Main logic and orchestration
- `sql.py` — Database interaction utilities
- `requirements.txt` — Python dependencies
- `visa_transactions.db` — SQLite database with Visa transaction data

