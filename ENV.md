# Environment setup

Create a `.env` file in the project root with your Google API key. Example:

```
GOOGLE_API_KEY=your_api_key_here
```

Notes:
- The application reads `GOOGLE_API_KEY` from the environment using `python-dotenv`.
- Do NOT commit your `.env` file to the repository. This project includes a `.gitignore` entry for `.env`.
- To run the app:

```bash
pip install -r requirements.txt
streamlit run chatbot.py
```
