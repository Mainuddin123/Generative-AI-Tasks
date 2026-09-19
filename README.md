# ✈️ AI Travel Planner

An AI-powered travel planning application that generates personalized travel itineraries using **Google Gemini**, **LangChain**, **Pydantic**, and **Streamlit**.

The application takes a destination, budget, number of days, and travel interests, then generates a structured day-wise travel plan.

---

## 🚀 Features

- 📍 Destination overview
- 📅 Day-wise travel itinerary
- 🌅 Morning, afternoon, and evening activities
- 🍴 Daily food recommendations
- 💰 Estimated trip budget
- 🎯 Recommended activities
- 💡 Travel tips
- 🤖 Google Gemini-powered generation
- 🧩 LangChain prompt pipeline
- 📦 Structured Pydantic output
- 🎨 Responsive Streamlit UI
- 🔄 Generate / Regenerate travel plans

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- LangChain Core
- Google Gemini
- Pydantic
- python-dotenv

---

## 📂 Project Structure

```text
GenAI-Task-1/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd GenAI-Task-1

2. Create a Virtual Environment
python -m venv venv
3. Activate the Virtual Environment

Windows:

venv\Scripts\activate
4. Install Dependencies
pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the project root:

GOOGLE_API_KEY=your_google_gemini_api_key

The .gitignore file excludes .env from version control.

▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

🧠 How It Works

The application follows this workflow:

User Input
    ↓
Destination
Budget
Number of Days
Interests
    ↓
LangChain Prompt
    ↓
Google Gemini
    ↓
Pydantic Output Parser
    ↓
Structured TravelPlan
    ↓
Streamlit UI

Input

The user provides:

Destination
Budget
Number of days
Interests
Processing

LangChain creates the prompt and sends it to Google Gemini.

The response is structured using Pydantic models.

Output

The application displays:

Destination overview
Day-wise itinerary
Food suggestions
Estimated budget
Activities
Travel tips
📦 Data Models

The application uses two Pydantic models.

DayPlan:

class DayPlan(BaseModel):
    day: int
    morning: str
    afternoon: str
    evening: str
    food_suggestions: List[str]


    TravelPlan:

    class TravelPlan(BaseModel):
    destination_overview: str
    itinerary: List[DayPlan]
    estimated_budget: str
    activities: List[str]
    food_suggestions: List[str]
    travel_tips: List[str]

These models ensure that the generated response follows a structured format.


🔗 LangChain Pipeline

The application uses the following LangChain pipeline:

travel_chain = (
    prompt
    | llm
    | parser
)

The pipeline consists of:

Chat Prompt Template
Google Gemini Chat Model
Pydantic Output Parser

🎨 User Interface

The Streamlit interface provides:

Dark themed design
Gradient branding
Two-column travel input form
Styled itinerary cards
Trip summary cards
Food and activity sections
Travel tips
Responsive layout

🧪 Example

Input
Destination: Hyderabad
Budget: ₹25,000
Number of Days: 3
Interests: Food, history, shopping, photography

Generated Output:

Destination Overview

Day 1
├── Morning
├── Afternoon
├── Evening
└── Food Suggestions

Day 2
├── Morning
├── Afternoon
├── Evening
└── Food Suggestions

Day 3
├── Morning
├── Afternoon
├── Evening
└── Food Suggestions

Trip Summary
├── Estimated Budget
├── Activities
├── Food Suggestions
└── Travel Tips

🔄 Regenerate Travel Plan

The application supports regenerating the itinerary with a different budget.

For example:

Initial Budget: ₹15,000
New Budget: ₹25,000

The user can change the budget and click:

✈️ Generate / Regenerate Travel Plan

The application generates a new travel plan based on the updated budget.

🔐 Security

API credentials are loaded through environment variables.

Sensitive files such as .env and the virtual environment are excluded using .gitignore.

Never expose your Google API key in source code or commit it to a public repository.


📌 Future Improvements
🗺️ Interactive maps
🏨 Hotel recommendations
🚆 Transportation planning
🌦️ Weather information
💱 Currency conversion
📍 Location-based recommendations
🖼️ Destination images
📄 Downloadable travel plans
🗓️ Calendar integration
👨‍💻 Author

Shaik Khaja Mainuddin

AI & Data Science Graduate

📄 License

This project is created for educational and portfolio purposes.
