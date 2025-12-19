# Portfolio Streamlit App  https://mein-portfolio.streamlit.app/

## Overview
A personal portfolio built with **Streamlit** showcasing projects, skills, and a donation button.

## Prerequisites
- Python 3.11 (or newer)
- pip

## Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd <repo-directory>

# Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Run Locally
```bash
streamlit run "portfolio+d.py" --server.headless true
```
The app will be available at `http://localhost:8501`.

## Deploy to Streamlit Cloud (recommended)
1. Push the repository to GitHub.
2. Sign in to [Streamlit Cloud](https://share.streamlit.io/).
3. Click **New app**, select the repository and branch, and set the **Main file path** to `portfolio+d.py`.
4. Click **Deploy**.

## CI with GitHub Actions
A GitHub Actions workflow (`.github/workflows/deploy.yml`) runs on every push to `main` and performs a sanity check by installing the dependencies and executing the app in head‑less mode. The workflow will pass if there are no import or runtime errors.

## License
This project is open source and available under the MIT License.

