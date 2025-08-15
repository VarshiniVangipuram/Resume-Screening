from flask import Flask, render_template, request, redirect, url_for
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk
import PyPDF2

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Predefined job descriptions and required skills
JOB_OPTIONS = {
    "Python Developer": {"python", "machine learning", "data analysis", "sql", "software development"},
    "Data Scientist": {"python", "machine learning", "data analysis", "statistics", "sql"},
    "Java Developer": {"java", "software development", "spring", "hibernate", "sql"},
    "Machine Learning Engineer": {"python", "machine learning", "deep learning", "data analysis", "tensorflow"},
    "Software Engineer": {"python", "java", "software development", "git", "sql"},
}

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Preprocess text (tokenization, stop word removal, and stemming)
def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    return set(stemmed_tokens)

# Extract skills from resume and match with job options
def match_skills_and_jobs(resume_text):
    resume_skills = preprocess_text(resume_text)
    job_matches = {}

    for job, required_skills in JOB_OPTIONS.items():
        matched_skills = resume_skills.intersection(required_skills)
        if matched_skills:
            job_matches[job] = {
                "matched_skills": matched_skills,
                "match_percentage": len(matched_skills) / len(required_skills) * 100,
            }

    # Sort jobs by match percentage (highest first)
    sorted_job_matches = sorted(job_matches.items(), key=lambda x: x[1]["match_percentage"], reverse=True)
    return sorted_job_matches

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'resume' not in request.files:
            return redirect(request.url)
        file = request.files['resume']
        if file.filename == '':
            return redirect(request.url)
        if file:
            # Check if the file is a PDF
            if file.filename.endswith('.pdf'):
                resume_text = extract_text_from_pdf(file)
            else:
                resume_text = file.read().decode('utf-8')
            job_matches = match_skills_and_jobs(resume_text)
            return render_template('index.html', job_matches=job_matches)
    return render_template('index.html', job_matches=None)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)