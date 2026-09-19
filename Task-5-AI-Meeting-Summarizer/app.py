import streamlit as st
import json
import html
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Meeting Summarizer",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# GLOBAL CSS
# ============================================================

st.html(
    """
    <style>

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(
                circle at 10% 0%,
                rgba(110, 40, 180, 0.18),
                transparent 35%
            ),
            radial-gradient(
                circle at 90% 10%,
                rgba(0, 180, 220, 0.10),
                transparent 35%
            ),
            #050b0f;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stAppViewBlockContainer"] {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 1100px !important;
    }

    .block-container {
        padding-top: 1rem !important;
    }

    .rainbow-text {
        background: linear-gradient(
            90deg,
            #ff00cc,
            #ff7a00,
            #ffee00,
            #39ff14,
            #00e5ff,
            #7a5cff,
            #ff00cc
        );

        background-size: 300% 300%;

        -webkit-background-clip: text;
        background-clip: text;

        -webkit-text-fill-color: transparent;

        animation: rainbowMove 6s ease infinite;
    }

    @keyframes rainbowMove {

        0% {
            background-position: 0% 50%;
        }

        50% {
            background-position: 100% 50%;
        }

        100% {
            background-position: 0% 50%;
        }

    }

    .hero {
        border: 1px solid rgba(190, 60, 255, 0.45);
        border-radius: 18px;

        padding: 30px 34px;

        margin-bottom: 32px;

        background: rgba(28, 22, 45, 0.82);

        box-shadow:
            0 0 35px rgba(160, 40, 255, 0.08);
    }

    .hero-title {
        font-size: 32px;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .hero-subtitle {
        color: #e2e5e9;
        font-size: 14px;
        line-height: 1.8;
    }

    .section-title {
        color: white;
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 25px;
    }

    .field-title {
        color: white;
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .field-description {
        color: #9eabb8;
        font-size: 12px;
        margin-bottom: 8px;
    }

    div.stButton > button {
        border: none !important;

        border-radius: 9px !important;

        padding: 11px 22px !important;

        color: white !important;

        font-weight: 700 !important;

        background:
            linear-gradient(
                90deg,
                #a52cff,
                #ff00b7
            ) !important;

        box-shadow:
            0 8px 22px rgba(200, 0, 255, 0.22);

        transition: 0.25s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 10px 28px rgba(255, 0, 200, 0.35);
    }

    .info-box {
        margin-top: 28px;

        padding: 22px 25px;

        border: 1px solid transparent;

        border-radius: 14px;

        background:
            linear-gradient(
                #161226,
                #161226
            ) padding-box,
            linear-gradient(
                90deg,
                #ff00cc,
                #00e5ff,
                #39ff14,
                #ff00cc
            ) border-box;
    }

    .info-title {
        font-size: 17px;
        font-weight: 800;
        margin-bottom: 18px;
    }

    .info-item {
        color: #d5dce3;
        font-size: 13px;
        line-height: 2;
    }

    .result-box {
        margin-top: 30px;

        padding: 24px;

        border: 1px solid rgba(0, 229, 255, 0.40);

        border-radius: 14px;

        background: rgba(10, 16, 23, 0.88);
    }

    .result-title {
        font-size: 21px;
        font-weight: 800;
        margin-bottom: 20px;
    }

    .result-heading {
        color: white;
        font-size: 15px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 8px;
    }

    .result-text {
        color: #d7dde4;
        font-size: 13px;
        line-height: 1.7;
    }

    .result-list {
        color: #d7dde4;
        font-size: 13px;
        line-height: 1.8;
    }

    .footer {
        margin-top: 55px;

        padding-top: 22px;

        border-top: 1px solid rgba(255,255,255,0.14);

        text-align: center;

        color: #7e8a96;

        font-size: 11px;

        line-height: 2;
    }

    </style>
    """
)


# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div class="hero">

        <div class="hero-title rainbow-text">
            📝 AI Meeting Summarizer
        </div>

        <div class="hero-subtitle">
            Transform lengthy meeting transcripts into concise,
            structured summaries using LangChain + Google Gemini.
            <br>
            Extract key points, decisions and action items automatically.
        </div>

    </div>
    """
)


# ============================================================
# MAIN TITLE
# ============================================================

st.html(
    """
    <div class="section-title">
        📝 Meeting Summary
    </div>
    """
)


# ============================================================
# INPUT LABEL
# ============================================================

st.html(
    """
    <div class="field-title">
        💬 Meeting Transcript
    </div>

    <div class="field-description">
        Paste your meeting transcript below
    </div>
    """
)


# ============================================================
# TEXT INPUT
# ============================================================

transcript = st.text_area(
    "Meeting Transcript",
    label_visibility="collapsed",
    height=240,
    placeholder="""Example:

John: We need to complete the website redesign by Friday.
Sarah: I will handle the frontend changes.
Mike: I will prepare the database updates.
John: Let's review everything on Thursday.
Sarah: We also discussed improving page loading speed.""",
)


# ============================================================
# BUTTON
# ============================================================

generate = st.button(
    "🚀 Generate Meeting Summary",
    type="primary",
)


# ============================================================
# API KEY
# ============================================================

def get_api_key():
    """
    Get GOOGLE_API_KEY from Streamlit Secrets
    or environment variables.
    """

    api_key = None

    try:
        api_key = st.secrets.get("GOOGLE_API_KEY")
    except Exception:
        api_key = None

    if not api_key:
        import os
        api_key = os.getenv("GOOGLE_API_KEY")

    return api_key


# ============================================================
# GENERATE SUMMARY
# ============================================================

def generate_summary(transcript_text):

    api_key = get_api_key()

    if not api_key:
        st.error("GOOGLE_API_KEY is missing from Streamlit Secrets.")
        return None

    try:
        parser = JsonOutputParser()

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are an expert meeting analysis assistant.

Analyze the meeting transcript provided by the user.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "summary": "Concise meeting summary",
    "key_points": [
        "Important point 1",
        "Important point 2"
    ],
    "decisions": [
        "Decision 1"
    ],
    "action_items": [
        "Action item 1"
    ]
}}

Rules:
- Return JSON only.
- Do not use Markdown.
- Do not use code fences.
- Do not add text before or after the JSON.
- Do not invent information.
- If there are no decisions, return an empty list.
- If there are no action items, return an empty list.
- If there are no key points, return an empty list.

{format_instructions}
""",
                ),
                (
                    "human",
                    """
Meeting Transcript:

{transcript}
""",
                ),
            ]
        )

        models = [
            "gemini-3.6-flash",
            "gemini-2.5-flash",
            "gemini-3.5-flash-lite",
        ]

        last_error = None

        for model_name in models:

            try:
                llm = ChatGoogleGenerativeAI(
                    model=model_name,
                    google_api_key=api_key,
                    temperature=0.2,
                )

                chain = prompt | llm | parser

                result = chain.invoke(
                    {
                        "transcript": transcript_text,
                        "format_instructions": parser.get_format_instructions(),
                    }
                )

                return result

            except Exception as model_error:

                last_error = model_error

                error_text = str(model_error)

                if (
                    "429" in error_text
                    or "RESOURCE_EXHAUSTED" in error_text
                ):
                    continue

                raise model_error

        st.error(
            "All configured Gemini models have exhausted their available quota."
        )

        return None

    except Exception as e:

        st.error(f"Error generating summary: {e}")

        return None


# ============================================================
# RESULT
# ============================================================

if generate:

    if not transcript.strip():

        st.warning(
            "Please enter a meeting transcript first."
        )

    else:

        with st.spinner(
            "Generating meeting summary..."
        ):

            result = generate_summary(
                transcript.strip()
            )

        if result:

            # ------------------------------------------------
            # SAFE DATA EXTRACTION
            # ------------------------------------------------

            summary = html.escape(
                str(
                    result.get(
                        "summary",
                        "No summary available.",
                    )
                )
            )

            key_points = result.get(
                "key_points",
                [],
            )

            decisions = result.get(
                "decisions",
                [],
            )

            action_items = result.get(
                "action_items",
                [],
            )

            # ------------------------------------------------
            # ENSURE LIST TYPES
            # ------------------------------------------------

            if not isinstance(key_points, list):
                key_points = [key_points]

            if not isinstance(decisions, list):
                decisions = [decisions]

            if not isinstance(action_items, list):
                action_items = [action_items]

            # ------------------------------------------------
            # SAFE HTML LISTS
            # ------------------------------------------------

            key_points_html = "".join(
                f"<li>{html.escape(str(item))}</li>"
                for item in key_points
            )

            decisions_html = "".join(
                f"<li>{html.escape(str(item))}</li>"
                for item in decisions
            )

            action_items_html = "".join(
                f"<li>{html.escape(str(item))}</li>"
                for item in action_items
            )

            # ------------------------------------------------
            # RESULT UI
            # ------------------------------------------------

            st.html(
                f"""
                <div class="result-box">

                    <div class="result-title rainbow-text">
                        📋 Generated Meeting Summary
                    </div>

                    <div class="result-heading">
                        📝 Summary
                    </div>

                    <div class="result-text">
                        {summary}
                    </div>

                    <div class="result-heading">
                        💡 Key Points
                    </div>

                    <ul class="result-list">
                        {key_points_html}
                    </ul>

                    <div class="result-heading">
                        ✅ Decisions
                    </div>

                    <ul class="result-list">
                        {decisions_html}
                    </ul>

                    <div class="result-heading">
                        📌 Action Items
                    </div>

                    <ul class="result-list">
                        {action_items_html}
                    </ul>

                </div>
                """
            )


# ============================================================
# HOW IT WORKS
# ============================================================

st.html(
    """
    <div class="info-box">

        <div class="info-title rainbow-text">
            ⚙️ How it works
        </div>

        <div class="info-item">
            📝 Meeting Transcript
        </div>

        <div class="info-item">
            ➜ Prompt Template
        </div>

        <div class="info-item">
            ➜ Gemini 3.5 Flash
        </div>

        <div class="info-item">
            ➜ JSON Output Parsing
        </div>

        <div class="info-item">
            ➜ Summary + Key Points + Decisions + Action Items
        </div>

    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="footer">

        <div class="rainbow-text">
            📝 AI Meeting Summarizer
        </div>

        <div>
            Built with Python • LangChain • Google Gemini • Streamlit
        </div>

    </div>
    """
)