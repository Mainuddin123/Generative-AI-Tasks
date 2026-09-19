# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built with Python, Streamlit, LangChain, and Google Gemini.

The application analyzes a candidate's resume against a given job description and generates a structured analysis of skills, experience, gaps, improvement suggestions, and interview preparation areas.

## 🚀 Features

- 📄 Upload resume in PDF or DOCX format
- 💼 Paste a job description
- 🤖 AI-powered resume analysis using Google Gemini
- 📊 Estimated resume-to-job match percentage
- ✅ Matching skills identification
- ❌ Missing skills identification
- 💡 Resume improvement suggestions
- 📚 Relevant experience and project identification
- 🎯 Interview preparation recommendations
- 📝 Final resume analysis summary
- 🎨 Dark-themed Streamlit interface

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini
- PyPDF
- python-docx

## 📂 Project Structure

    Task-2-AI-Resume-Analyzer/
    ├── app.py
    ├── requirements.txt
    └── README.md

## ⚙️ Installation

Clone the repository:

    git clone https://github.com/Mainuddin123/Generative-AI-Tasks.git

Navigate to the project:

    cd Generative-AI-Tasks/Task-2-AI-Resume-Analyzer

Create a virtual environment:

    python -m venv venv

Activate the environment on Windows:

    venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

## 🔑 API Key Configuration

The application requires a Google Gemini API key.

Create a `.env` file and add:

    GOOGLE_API_KEY=your_google_gemini_api_key

Never commit your API key to GitHub.

## ▶️ Run the Application

Run:

    streamlit run app.py

The application will be available at:

    http://localhost:8501

## 📋 How to Use

1. Upload your resume.
2. Paste the target job description.
3. Click **Analyze Resume**.
4. The application extracts the resume content.
5. Gemini analyzes the resume against the job description.
6. Review the generated resume analysis.

## 📊 Analysis Output

The application generates the following sections:

### 1. Overall Match
Provides an estimated percentage match between the resume and the job description with supporting reasoning.

### 2. Matching Skills
Identifies skills and technologies present in the resume that match the job requirements.

### 3. Missing Skills
Identifies important requirements from the job description that are not clearly demonstrated in the resume.

### 4. Relevant Experience & Projects
Highlights resume projects and experience relevant to the target role.

### 5. Resume Strengths
Identifies key areas of the resume that align with the job requirements.

### 6. Improvement Suggestions
Provides practical recommendations for improving the resume's alignment with the target position.

### 7. Interview Preparation
Suggests technical concepts and areas to prepare based on the job description.

### 8. Final Summary
Provides a concise overall summary of the resume analysis.

## 🔐 Security

- Never commit API keys or other secrets.
- Keep `.env` files private.
- Add `.env` to `.gitignore`.

## 👨‍💻 Author

**Shaik Khaja Mainuddin**

GitHub: https://github.com/Mainuddin123

## 📌 Project

This project is part of the **Generative AI Tasks** project series.

Repository: https://github.com/Mainuddin123/Generative-AI-Tasks
