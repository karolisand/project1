# Project1: Vilnius RAG Demo with LangChain & Streamlit

## Overview

This application is a Retrieval-Augmented Generation (RAG) demo built with [LangChain](https://python.langchain.com/) and [Streamlit](https://streamlit.io/). It fetches and processes information about Vilnius from the web and local files, splits the data into chunks, embeds it using OpenAI-compatible models, and allows users to ask questions about Vilnius via a simple web interface. The app uses vector search to retrieve relevant context for each query and generates answers using a hosted AI model.

## Features
- Loads and processes data from Wikipedia, Faktograma, and a local file (`Vilnius.txt`)
- Splits and embeds documents for efficient retrieval
- Uses OpenAI-compatible embeddings and chat models (via GitHub Models API)
- Interactive Q&A interface with Streamlit
- Displays sources for each answer

## Requirements
- Python 3.12+
- An OpenAI-compatible API key (see below)

## Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd project1
   ```
2. **Install dependencies:**
   You can use [uv](https://github.com/astral-sh/uv) (recommended) or pip:
   ```bash
   uv pip install -r pyproject.toml
   # or, if you use pip:
   pip install -r requirements.txt  # (generate this from pyproject.toml if needed)
   ```

## Environment Setup
This app requires an API key for the GitHub Models (OpenAI-compatible) endpoint. You must set the `OPENAI_SECRET` environment variable.

1. **Create a `.env` file in the project root:**
   ```env
   OPENAI_SECRET=your_github_models_api_key_here
   ```
   Replace `your_github_models_api_key_here` with your actual key.

2. **Alternatively, export the variable in your shell:**
   ```bash
   export OPENAI_SECRET=your_github_models_api_key_here
   ```

## Running the App
Start the Streamlit app with:
```bash
streamlit run main.py
```
Then open the provided local URL in your browser.

## Main Libraries Used
- [LangChain](https://python.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Project Structure
- `main.py` — Main application code
- `Vilnius.txt` — Local text file with additional info
- `temp/` — (Optional) Temporary scripts or files

## Notes
- The app uses the [GitHub Models API](https://models.github.ai/) for both embeddings and chat completions. You need access and a valid API key.
- All data is loaded at startup; for large files or more sources, consider batching or async loading.

---
Feel free to contribute or open issues!