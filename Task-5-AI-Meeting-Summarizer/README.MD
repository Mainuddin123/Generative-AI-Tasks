# 🤖 AI Meeting Summarizer

An AI-powered application that converts meeting transcripts into concise, structured summaries using LangChain and Google Gemini.

## 🚀 Features

- 📝 Meeting transcript input
- 🤖 AI-powered summarization
- 💡 Key point extraction
- ✅ Decision extraction
- 📌 Action item extraction
- 📋 Structured JSON output
- 🎨 Modern Streamlit UI
- 🌈 Rainbow-gradient styling
- ⚡ Google Gemini integration through LangChain

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini
- Prompt Templates
- JSON Output Parsing

## 🔄 Workflow

Meeting Transcript → Prompt Template → Google Gemini → JSON Output Parsing → Structured Meeting Summary

## 📂 Project Structure

Task-5-AI-Meeting-Summarizer/
├── app.py
├── requirements.txt
└── README.md

## ⚙️ Installation

Clone the repository:

    git clone https://github.com/Mainuddin123/Generative-AI-Tasks.git

Navigate to the project:

    cd Generative-AI-Tasks/Task-5-AI-Meeting-Summarizer

Create a virtual environment:

    python -m venv venv

Activate the environment on Windows:

    venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

## 🔐 API Key Configuration

Create:

    .streamlit/secrets.toml

Add your Google Gemini API key:

    GOOGLE_API_KEY = "your_google_gemini_api_key"

Never upload your API key to GitHub.

## ▶️ Run the Application

    streamlit run app.py

## 🧪 Example Input

    Designer: I finished the login and dashboard screens.
    
    Tester: I will start testing the authentication flow tomorrow.
    
    Project Manager: The backend team must finish authentication by Friday.
    
    Developer: I will complete the authentication testing by Friday.
    
    Designer: I will provide the final UI assets by Thursday.
    
    Project Manager: Let's have a final review meeting on Friday afternoon.

## 📤 Example Output

### Summary

The team discussed progress and deadlines for the upcoming application launch, focusing on backend authentication, UI assets, testing schedules, and the final review.

### Key Points

- Login and dashboard screens are completed.
- Authentication testing is scheduled to begin.
- Backend authentication must be completed by Friday.
- Final UI assets will be provided by Thursday.

### Decisions

- Backend authentication must be finished by Friday.
- A final review meeting will be held on Friday afternoon.

### Action Items

- Tester: Start authentication testing.
- Developer: Complete authentication testing by Friday.
- Designer: Provide final UI assets by Thursday.
- Team: Attend the final review meeting.

## 🧠 How It Works

1. User provides a meeting transcript.
2. The transcript is passed into a LangChain prompt template.
3. Google Gemini processes the meeting content.
4. The model returns structured JSON.
5. The application parses the JSON response.
6. The UI displays the summary, key points, decisions, and action items.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Generative AI
- LLM application development
- Prompt engineering
- LangChain
- Google Gemini API
- Structured LLM output
- JSON parsing
- Streamlit
- AI application development

## 🌐 Deployment

The application can be deployed using Streamlit Community Cloud.

Configure the Streamlit secret:

    GOOGLE_API_KEY = "your_google_gemini_api_key"

## 👨‍💻 Author

**Shaik Khaja Mainuddin**

Built with Python • LangChain • Google Gemini • Streamlit
