# 🤖 AI SQL Query Generator

An AI-powered SQL Query Generator that converts natural-language questions into SQL queries using **LangChain + Google Gemini 3.5 Flash**.

The application allows users to provide a database schema and ask questions in plain English. Gemini generates the corresponding SQL query along with an explanation and the tables used.

## 🚀 Features

- 🗄️ Accept custom database schemas
- 💬 Ask questions using natural language
- 🤖 Generate SQL using Google Gemini 3.5 Flash
- 🔗 LangChain integration
- 🧠 Prompt-based SQL generation
- 📋 Structured JSON output parsing
- 📝 SQL query explanation
- 📊 Displays tables used in the generated query
- 🎨 Professional Streamlit UI
- 🔐 Secure API key configuration

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini 3.5 Flash
- python-dotenv

## 📂 Project Structure

Task-4-AI-SQL-Query-Generator/
├── app.py
├── requirements.txt
└── README.md

## ⚙️ How It Works

Database Schema + Natural Language Question
                    ↓
              Prompt Template
                    ↓
          Google Gemini 3.5 Flash
                    ↓
          Structured JSON Output
                    ↓
      SQL Query + Explanation + Tables Used

## 🔑 Environment Variable

Create a `.env` file in the project directory:

GOOGLE_API_KEY=your_google_api_key

Never commit your API key to GitHub.

## ▶️ Run Locally

Clone the repository:

git clone https://github.com/Mainuddin123/Generative-AI-Tasks.git

Navigate to the project:

cd Generative-AI-Tasks/Task-4-AI-SQL-Query-Generator

Create a virtual environment:

python -m venv venv

Activate the environment on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

## 💡 Example

### Database Schema

CREATE TABLE customers (
    customer_id INT,
    name VARCHAR(100),
    email VARCHAR(150),
    city VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    status VARCHAR(50)
);

### Natural Language Question

Show the total order amount for each customer from Hyderabad.

### Generated SQL

SELECT
    c.customer_id,
    c.name,
    SUM(o.amount) AS total_order_amount
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
WHERE c.city = 'Hyderabad'
GROUP BY c.customer_id, c.name;

### Explanation

The generated query joins the customers and orders tables using customer_id, filters customers from Hyderabad, calculates the total order amount, and groups the results by customer.

## 🔒 Security

- API keys are loaded through environment variables.
- `.env` should not be committed to GitHub.
- Add `.env` to `.gitignore`.
- Never expose API keys in source code.

## 🎯 Project Purpose

This project demonstrates how Generative AI can be used to convert natural-language database questions into SQL queries.

It showcases the integration of:

- Large Language Models
- Prompt Engineering
- LangChain
- Structured Output Parsing
- Google Gemini
- Streamlit

## 👨‍💻 Author

**Shaik Khaja Mainuddin**

GitHub: https://github.com/Mainuddin123

LinkedIn: https://www.linkedin.com/in/khaja-mainuddin-sk-958436348

---

⭐ Built with Python • LangChain • Google Gemini • Streamlit
