# 💬 AI Customer Support Chatbot

An AI-powered customer support chatbot built with **Python, Streamlit, LangChain, and Google Gemini**.

The application generates professional customer support responses based **only on the provided support policy**, helping prevent unsupported information from being invented.

## 🚀 Features

- 💬 Customer question input
- 📋 Custom support policy input
- 🤖 Google Gemini-powered responses
- 🔗 LangChain integration
- 🛡️ Policy-based response generation
- 🚫 Prevents unsupported policy assumptions
- ⚡ Interactive Streamlit interface
- 🎨 Custom dark-themed UI
- ❌ Error handling for missing API keys and runtime errors

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini
- python-dotenv

## 📁 Project Structure

    Task-3-AI-Customer-Support-Chatbot/
    ├── app.py
    ├── requirements.txt
    └── README.md

## ⚙️ Installation

Clone the repository:

    git clone https://github.com/Mainuddin123/Generative-AI-Tasks.git

Navigate to the project:

    cd Generative-AI-Tasks/Task-3-AI-Customer-Support-Chatbot

Create a virtual environment:

    python -m venv venv

Activate the virtual environment on Windows:

    venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

## 🔑 API Key Configuration

Create a `.env` file inside the project directory:

    GOOGLE_API_KEY=your_google_gemini_api_key

Do not upload your `.env` file or expose your API key publicly.

## ▶️ Run the Application

Start the Streamlit application:

    streamlit run app.py

The application will open in your browser.

## 🧪 Example

### Customer Question

    I received the wrong product. Can I get a refund?

### Support Policy

    Refund Policy:
    Customers can request a refund within 7 days of delivery.
    The product must be unused and in its original condition.

    Order Policy:
    Customers can check order status using their order ID.

    Shipping Policy:
    Standard shipping takes 3-5 business days.

### Example Response

    You can request a refund within 7 days of delivery,
    provided the product is unused and in its original condition.

    Please note that specific information regarding receiving
    a wrong product is not available in the provided policy.

## 🧠 How It Works

    Customer Question
            ↓
    Support Policy
            ↓
       LangChain
            ↓
      Google Gemini
            ↓
    Policy-based Response
            ↓
      Streamlit UI

The chatbot is instructed to use **only the supplied support policy**. If the policy does not contain enough information to answer a question, the chatbot informs the customer instead of creating unsupported policy information.

## 🔐 Error Handling

The application handles:

- Missing `GOOGLE_API_KEY`
- Empty customer questions
- Empty support policies
- Gemini/LangChain runtime errors
- Structured Gemini response content

## 📌 Task Information

**Generative AI Tasks – Task 3**

**Project:** AI Customer Support Chatbot

**Built with:** Python • LangChain • Google Gemini • Streamlit

## 👨‍💻 Author

**Shaik Khaja Mainuddin**

GitHub: https://github.com/Mainuddin123

LinkedIn: https://www.linkedin.com/in/khaja-mainuddin-sk-958436348
