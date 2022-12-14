# JAD Solutions (Team 1) Streamlit & FastAPI application

## Getting started
### Requirements
- Python 3.10

### Project setup
1. Create a Python venv: `python -m venv venv`
	
2. Activate the venv using the following command
	- `.\venv\Scripts\Activate`
	
3. Install the dependencies: `pip install -r requirements.txt`

4. Run the code:
   - To run Streamlit:
     - `streamlit run .\main.py` in a console window
     - A browser window should open
   - To run FastAPI:
     - `uvicorn tanks_api:app --reload` in a console window
     - Navigate to: http://127.0.0.1:8000