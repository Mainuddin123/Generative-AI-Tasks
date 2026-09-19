import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv()

st.set_page_config(
    page_title="AI Customer Support Chatbot",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background:
            radial-gradient(circle at top left, #17122f 0%, #070b11 45%, #06171b 100%);
        color: white;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    [data-testid="stDecoration"] {
        display: none;
    }

    .block-container {
        max-width: 900px !important;
        padding-top: 2.8rem !important;
        padding-bottom: 2rem !important;
    }

    /* ---------- HERO ---------- */

    .hero-box {
        background: rgba(27, 25, 43, 0.92);
        border: 1px solid #41375a;
        border-radius: 20px;
        padding: 28px 30px;
        margin-bottom: 42px;
    }

    .hero-title {
    font-size: 36px !important;
    font-weight: 800 !important;
    margin: 0 0 12px 0 !important;
    color: #d83cff !important;
}

.hero-subtitle {
    color: #e4e0ed !important;
    font-size: 14px !important;
    line-height: 1.8 !important;
    margin: 0 !important;
}

    /* ---------- SECTION ---------- */

    .section-title {
        font-size: 25px;
        font-weight: 800;
        color: white;
        margin-bottom: 25px;
    }

    .field-title {
        font-size: 18px;
        font-weight: 800;
        color: white;
        margin-bottom: 8px;
    }

    .field-label {
        color: #aeb4c5;
        font-size: 13px;
        margin-bottom: 8px;
    }

    /* ---------- TEXT AREAS ---------- */

    textarea {
        background-color: #f1f3f7 !important;
        color: #596273 !important;
        border-radius: 8px !important;
        border: none !important;
        font-size: 13px !important;
    }

    textarea::placeholder {
        color: #8b95a8 !important;
        opacity: 1 !important;
    }

    /* ---------- BUTTON ---------- */

    div.stButton > button {
        background: linear-gradient(90deg, #8d3cff, #ed27bf) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 11px 25px !important;
        font-weight: 700 !important;
        font-size: 13px !important;
        box-shadow: 0 8px 25px rgba(205, 38, 218, 0.25);
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #a14aff, #ff35ca) !important;
        color: white !important;
        border: none !important;
    }

    /* ---------- RESULT ---------- */

    .result-box {
        background: rgba(27, 25, 43, 0.9);
        border: 1px solid #41375a;
        border-radius: 15px;
        padding: 22px;
        margin-top: 25px;
        color: #eeeeee;
        line-height: 1.7;
    }

    .result-title {
        font-size: 20px;
        font-weight: 800;
        color: white;
        margin-bottom: 12px;
    }

    /* ---------- FOOTER ---------- */

    .custom-footer {
        border-top: 1px solid #2b3040;
        margin-top: 70px;
        padding-top: 18px;
        text-align: center;
        color: #77809a;
        font-size: 11px;
        line-height: 1.8;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
    """
    <div class="hero-box">
        <p class="hero-title">📄 AI Customer Support Chatbot</p>
        <p class="hero-subtitle">
            Get intelligent customer support responses using
            LangChain + Google Gemini.
            <br>
            Analyze orders, refunds, shipping and product-related questions.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)



# ============================================================
# CUSTOMER SUPPORT SECTION
# ============================================================

st.markdown(
    """
    <div class="section-title">
        💬 Customer Support
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# INPUT COLUMNS
# ============================================================

left, right = st.columns(2, gap="medium")

with left:

    st.markdown(
        """
        <div class="field-title">
            🛒 Customer Question
        </div>

        <div class="field-label">
            Enter customer question
        </div>
        """,
        unsafe_allow_html=True
    )

    customer_question = st.text_area(
        "Customer Question",
        placeholder=(
            "Example:\n"
            "I received the wrong product. Can I get a refund?"
        ),
        height=180,
        label_visibility="collapsed"
    )


with right:

    st.markdown(
        """
        <div class="field-title">
            📋 Support Policy
        </div>

        <div class="field-label">
            Enter support policy
        </div>
        """,
        unsafe_allow_html=True
    )

    support_policy = st.text_area(
        "Support Policy",
        value="""Refund Policy:
Customers can request a refund within 7 days of delivery.
The product must be unused and in its original condition.

Order Policy:
Customers can check order status using their order ID.

Shipping Policy:
Standard shipping takes 3-5 business days.""",
        height=180,
        label_visibility="collapsed"
    )

# ============================================================
# GEMINI FUNCTION
# ============================================================

def generate_support_response(question, policy):

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        return None, "GOOGLE_API_KEY is not configured."

    try:

        llm = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash",
            google_api_key=api_key,
            temperature=0.2
        )

        prompt = f"""
You are an AI Customer Support Assistant.

Your job is to answer the customer's question using ONLY
the provided customer support policy.

CUSTOMER QUESTION:
{question}

SUPPORT POLICY:
{policy}

Instructions:
1. Give a clear and professional response.
2. Follow the support policy.
3. Do not invent policies or information.
4. If the policy does not provide enough information,
   clearly say that the information is not available in
   the provided policy.
5. Keep the response concise and customer-friendly.
"""

        response = llm.invoke(prompt)

        answer = response.content

        # Handle Gemini structured content
        if isinstance(answer, list):

            text_parts = []

            for item in answer:

                if isinstance(item, dict) and "text" in item:
                    text_parts.append(item["text"])

                else:
                    text_parts.append(str(item))

            answer = "\n".join(text_parts)

        elif isinstance(answer, dict):

            answer = answer.get("text", str(answer))

        return answer, None

    except Exception as e:

        return None, str(e)


# ============================================================
# BUTTON
# ============================================================

st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

if st.button("🚀 Get Support Response"):

    if not customer_question.strip():
        st.warning("Please enter a customer question.")

    elif not support_policy.strip():
        st.warning("Please enter the support policy.")

    else:

        with st.spinner("Generating support response..."):

            answer, error = generate_support_response(
                customer_question.strip(),
                support_policy.strip()
            )

        if error:
            st.error(error)

        else:

            # Convert Gemini response safely to plain text
            if isinstance(answer, dict):
                answer = answer.get("text", str(answer))

            elif isinstance(answer, list):
                answer = "\n".join(
                    item.get("text", str(item)) if isinstance(item, dict) else str(item)
                    for item in answer)

            else:
                answer = str(answer)

            st.markdown(
                f"""
                <div class="result-box">
                <div class="result-title">
                💬 Support Response
               </div>
               {answer.replace(chr(10), "<br>")}
               </div>
               """,
               unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="custom-footer">
        © AI Customer Support Chatbot
        <br>
        Built with Python • LangChain • Google Gemini • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)