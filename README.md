# Resume Screening Web App

This is a Flask-based web application for automated resume screening. It extracts skills from uploaded resumes (PDF or text) and matches them to predefined job roles.

## Features

- Upload resume files (PDF or plain text)
- Extracts and preprocesses resume text using NLTK
- Matches resume skills to predefined job descriptions
- Displays job matches and match percentages

## Setup

1. **Clone the repository**  
   Download or clone this project to your local machine.

2. **Install dependencies**  
   Run the following command in your project directory:
   ```
   pip install -r requirements.txt
   ```

3. **Download NLTK data**  
   The app will automatically download required NLTK data (`punkt` and `stopwords`) on first run.

4. **Run the application**  
   ```
   python app.py
   ```
   The app will start on `http://127.0.0.1:5000/`.

## Usage

- Open the app in your browser.
- Upload a resume file (PDF or text).
- View matched job roles and skill match percentages.

## File Structure

- `app.py` — Main Flask application
- `requirements.txt` — Python dependencies
- `templates/index.html` — HTML template for the web interface
- `uploads/` — Folder for uploaded resumes

## Notes

- Only basic skill extraction and matching is implemented.
- For best results, upload resumes in PDF or plain text format.
- You can customize job roles and required skills in the `JOB_OPTIONS` dictionary in `app.py`.

## License

This project is for educational purposes and is licensed under the MIT License. See `LICENSE` for details.