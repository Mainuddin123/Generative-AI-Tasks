import os
import json
import re

import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv()

st.set_page_config(
    page_title="AI SQL Query Generator",
    page_icon="🗄️",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ================= GLOBAL ================= */

    .stApp {
        background:
            radial-gradient(
                circle at top left,
                #17122f 0%,
                #070b11 45%,
                #06171b 100%
            );
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


    /* ================= HERO ================= */

    .hero-box {
        background: rgba(27, 25, 43, 0.92);
        border: 1px solid #41375a;
        border-radius: 20px;
        padding: 28px 30px;
        margin-bottom: 42px;
    }

    .hero-title {
        font-size: 36px;
        font-weight: 800;
        margin: 0 0 12px 0;
        color: #d83cff;
    }

    .hero-subtitle {
        color: #e4e0ed;
        font-size: 14px;
        line-height: 1.8;
        margin: 0;
    }


    /* ================= SECTION ================= */

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


    /* ================= TEXT AREAS ================= */

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


    /* ================= BUTTON ================= */

    div.stButton > button {
        background: linear-gradient(
            90deg,
            #8d3cff,
            #ed27bf
        ) !important;

        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 11px 25px !important;
        font-weight: 700 !important;
        font-size: 13px !important;

        box-shadow:
            0 8px 25px rgba(205, 38, 218, 0.25);
    }

    div.stButton > button:hover {
        background: linear-gradient(
            90deg,
            #a14aff,
            #ff35ca
        ) !important;

        color: white !important;
        border: none !important;
    }


    /* ================= HOW IT WORKS ================= */

    .info-box {
        background: rgba(20, 18, 35, 0.9);
        border: 1px solid #41375a;
        border-radius: 10px;
        padding: 18px;
        margin-top: 24px;
    }

    .info-title {
        color: white;
        font-size: 14px;
        font-weight: 800;
        margin-bottom: 14px;
    }

    .info-content {
        background: #f1f3f7;
        color: #596273;
        border-radius: 7px;
        padding: 16px;
        font-size: 12px;
        line-height: 1.8;
    }

    .info-line {
        margin: 0;
        padding: 2px 0;
    }


    /* ================= RESULT ================= */

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

    .sql-box {
        background: #0b0f16;
        border: 1px solid #34384a;
        border-radius: 8px;
        padding: 15px;
        margin-top: 10px;
        overflow-x: auto;
    }

    .sql-box pre {
        margin: 0;
        white-space: pre-wrap;
        color: #e9edf7;
        font-family: Consolas, monospace;
        font-size: 13px;
    }


    /* ================= FOOTER ================= */

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
        <div class="hero-title">🗄️ AI SQL Query Generator</div>
        <div class="hero-subtitle">
            Convert natural-language questions into SQL queries
            using LangChain + Google Gemini.
            <br>
            Provide your database schema and ask a question in plain English.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# QUERY GENERATOR
# ============================================================

st.markdown(
    """
    <div class="section-title">
        🔍 Query Generator
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# INPUT COLUMNS
# ============================================================

left, right = st.columns(2, gap="medium")


# ============================================================
# DATABASE SCHEMA
# ============================================================

with left:

    st.markdown(
        """
        <div class="field-title">
            🗃️ Database Schema
        </div>
        <div class="field-label">
            Enter your database tables and columns
        </div>
        """,
        unsafe_allow_html=True
    )

    database_schema = st.text_area(
        "Database Schema",
        value="""CREATE TABLE customers (
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
);""",
        height=180,
        label_visibility="collapsed"
    )


# ============================================================
# NATURAL LANGUAGE QUESTION
# ============================================================

with right:

    st.markdown(
        """
        <div class="field-title">
            💬 Natural Language Question
        </div>
        <div class="field-label">
            Ask what data you want to retrieve
        </div>
        """,
        unsafe_allow_html=True
    )

    natural_question = st.text_area(
        "Natural Language Question",
        placeholder=(
            "Example:\n"
            "Show the total order amount for each customer from Hyderabad."
        ),
        height=180,
        label_visibility="collapsed"
    )


# ============================================================
# GEMINI FUNCTION
# ============================================================

def generate_sql(schema, question):

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        return (
            None,
            None,
            None,
            "GOOGLE_API_KEY is not configured."
        )

    try:

        # ----------------------------------------------------
        # GEMINI 3.5 FLASH
        # ----------------------------------------------------

        llm = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash",
            google_api_key=api_key,
            temperature=0.1
        )


        # ----------------------------------------------------
        # PROMPT
        # ----------------------------------------------------

        prompt = f"""
You are an expert SQL query generator.

Convert the user's natural-language question into a correct SQL query
using ONLY the provided database schema.

DATABASE SCHEMA:
{schema}

USER QUESTION:
{question}

IMPORTANT RULES:

1. Use only tables and columns that exist in the provided schema.
2. Do not invent tables or columns.
3. Generate standard SQL.
4. Determine appropriate JOIN conditions from the schema.
5. Return ONLY valid JSON.
6. Do not include markdown code fences.
7. Do not include additional text outside the JSON.

Return exactly this structure:

{{
    "sql_query": "SELECT ...",
    "explanation": "Brief explanation of the query.",
    "tables_used": ["table1", "table2"]
}}
"""


        # ----------------------------------------------------
        # CALL GEMINI
        # ----------------------------------------------------

        response = llm.invoke(prompt)

        content = response.content


        # ----------------------------------------------------
        # HANDLE GEMINI RESPONSE FORMAT
        # ----------------------------------------------------

        if isinstance(content, list):

            parts = []

            for item in content:

                if isinstance(item, dict):

                    if "text" in item:
                        parts.append(str(item["text"]))

                else:
                    parts.append(str(item))

            content = "\n".join(parts)


        content = str(content).strip()


        # ----------------------------------------------------
        # REMOVE MARKDOWN CODE FENCES
        # ----------------------------------------------------

        content = re.sub(
            r"^```json\s*",
            "",
            content,
            flags=re.IGNORECASE
        )

        content = re.sub(
            r"^```\s*",
            "",
            content
        )

        content = re.sub(
            r"\s*```$",
            "",
            content
        )

        content = content.strip()


        # ----------------------------------------------------
        # EXTRACT JSON OBJECT
        # ----------------------------------------------------

        start = content.find("{")
        end = content.rfind("}")

        if start != -1 and end != -1:
            content = content[start:end + 1]


        # ----------------------------------------------------
        # PARSE JSON
        # ----------------------------------------------------

        try:

            data = json.loads(content)

        except json.JSONDecodeError:

            return (
                None,
                None,
                None,
                "Gemini returned an invalid JSON response."
            )


        # ----------------------------------------------------
        # EXTRACT RESULTS
        # ----------------------------------------------------

        sql_query = str(
            data.get("sql_query", "")
        ).strip()

        explanation = str(
            data.get(
                "explanation",
                "SQL query generated from the provided schema."
            )
        ).strip()

        tables_used = data.get(
            "tables_used",
            []
        )

        if not isinstance(tables_used, list):
            tables_used = [str(tables_used)]


        return (
            sql_query,
            explanation,
            tables_used,
            None
        )


    except Exception as e:

        return (
            None,
            None,
            None,
            str(e)
        )


# ============================================================
# GENERATE BUTTON
# ============================================================

st.markdown(
    "<div style='height:18px'></div>",
    unsafe_allow_html=True
)


if st.button("🚀 Generate SQL Query"):

    if not database_schema.strip():

        st.warning(
            "Please enter the database schema."
        )

    elif not natural_question.strip():

        st.warning(
            "Please enter a natural-language question."
        )

    else:

        with st.spinner(
            "Generating SQL query..."
        ):

            sql_query, explanation, tables_used, error = generate_sql(
                database_schema.strip(),
                natural_question.strip()
            )


        if error:

            st.error(error)

        else:

            # =================================================
            # RESULT CARD
            # =================================================

            st.markdown(
                """
                <div class="result-box">
                    <div class="result-title">
                        🧾 Generated SQL Query
                    </div>
                """,
                unsafe_allow_html=True
            )


            # =================================================
            # SQL
            # =================================================

            st.markdown(
                f"""
                <div class="sql-box">
                    <pre>{sql_query}</pre>
                </div>
                """,
                unsafe_allow_html=True
            )


            # =================================================
            # EXPLANATION
            # =================================================

            st.markdown(
                f"""
                <div style="
                    margin-top:18px;
                    color:#e4e0ed;
                    font-size:14px;
                ">
                    <strong>💡 Explanation</strong>
                    <br><br>
                    {explanation}
                </div>
                """,
                unsafe_allow_html=True
            )


            # =================================================
            # TABLES USED
            # =================================================

            if tables_used:

                tables_text = ", ".join(
                    str(table)
                    for table in tables_used
                )

                st.markdown(
                    f"""
                    <div style="
                        margin-top:15px;
                        color:#e4e0ed;
                        font-size:13px;
                    ">
                        <strong>🗂️ Tables Used:</strong>
                        {tables_text}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    """
                    <div style="
                        margin-top:15px;
                        color:#e4e0ed;
                        font-size:13px;
                    ">
                        <strong>🗂️ Tables Used:</strong>
                        No tables identified.
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


# ============================================================
# HOW IT WORKS
# ============================================================

# IMPORTANT:
# Keep this as ONE HTML block.
# Do not put blank lines between nested HTML elements.

st.markdown(
    """
    <div class="info-box">
        <div class="info-title">How it works:</div>
        <div class="info-content">
            <div class="info-line">
                Database Schema + Natural Language Question
            </div>
            <div class="info-line">
                → Prompt Template
            </div>
            <div class="info-line">
                → Gemini 3.5 Flash
            </div>
            <div class="info-line">
                → JSON Output Parser
            </div>
            <div class="info-line">
                → SQL Query + Explanation + Tables Used
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="custom-footer">
        © AI SQL Query Generator
        <br><br>
        Built with Python • LangChain • Google Gemini • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
