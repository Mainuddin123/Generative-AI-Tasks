from dotenv import load_dotenv

load_dotenv()

from typing import List

import streamlit as st
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


# ============================================================
# 1. PYDANTIC OUTPUT SCHEMA
# ============================================================

class DayPlan(BaseModel):
    day: int = Field(description="Day number")
    morning: str = Field(description="Morning activities")
    afternoon: str = Field(description="Afternoon activities")
    evening: str = Field(description="Evening activities")
    food_suggestions: List[str] = Field(
        description="Food suggestions for the day"
    )


class TravelPlan(BaseModel):
    destination_overview: str
    itinerary: List[DayPlan]
    estimated_budget: str
    activities: List[str]
    food_suggestions: List[str]
    travel_tips: List[str]


# ============================================================
# 2. OUTPUT PARSER
# ============================================================

parser = PydanticOutputParser(
    pydantic_object=TravelPlan
)


# ============================================================
# 3. PROMPT TEMPLATE
# ============================================================

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert travel planner.

Create a personalized travel itinerary based on:
- Destination
- Budget
- Number of days
- Interests

Make the plan practical and organize it day by day.

{format_instructions}
"""
    ),
    (
        "human",
        """
Destination: {destination}

Budget: {budget}

Number of days: {days}

Interests: {interests}
"""
    )
])


# ============================================================
# 4. GEMINI MODEL
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.7
)


# ============================================================
# 5. LANGCHAIN CHAIN
# ============================================================

travel_chain = (
    prompt
    | llm
    | parser
)


# ============================================================
# 6. STREAMLIT CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# 7. CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

/* ==========================================================
   MAIN APPLICATION
   ========================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(120, 80, 255, 0.15),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(0, 200, 255, 0.12),
            transparent 30%
        ),
        #090b10;

    color: #f5f5f5;
}


/* ==========================================================
   MAIN CONTAINER
   ========================================================== */

.block-container {
    max-width: 1200px;
    padding-top: 0 !important;
    padding-bottom: 4rem;
}


/* ==========================================================
   STREAMLIT BRANDING
   ========================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ==========================================================
   HERO
   ========================================================== */

.hero {
    padding: 25px 35px 30px 35px;

    border-radius: 24px;

    background:
        linear-gradient(
            135deg,
            rgba(34, 34, 45, 0.95),
            rgba(16, 18, 27, 0.95)
        );

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.35);

    margin-bottom: 30px;
}


.hero-title {
    font-size: 48px;
    font-weight: 800;
    line-height: 1.15;

    background:
        linear-gradient(
            90deg,
            #ff4ecd,
            #8b7cff,
            #35d8ff,
            #55f5b2
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}


.hero-subtitle {
    color: #aeb4c0;
    font-size: 17px;
    line-height: 1.7;
    margin-top: 10px;
}


/* ==========================================================
   SECTION TITLES
   ========================================================== */

.section-title {
    font-size: 27px;
    font-weight: 750;
    margin-top: 30px;
    margin-bottom: 15px;
    color: #ffffff;
}


/* ==========================================================
   INPUT CARD
   ========================================================== */

.input-card {
    padding: 25px;

    border-radius: 20px;

    background: rgba(22, 25, 34, 0.95);

    border: 1px solid rgba(255,255,255,0.07);

    margin-bottom: 25px;
}


/* ==========================================================
   INPUT LABELS
   ========================================================== */

label {
    color: #d7dbe5 !important;
    font-weight: 600 !important;
}


/* ==========================================================
   INPUT FIELDS
   ========================================================== */

div[data-baseweb="input"] {
    background-color: #141821 !important;
    border: 1px solid #303644 !important;
    border-radius: 10px !important;
}


div[data-baseweb="input"]:focus-within {
    border-color: #8b7cff !important;
    box-shadow: 0 0 0 1px #8b7cff !important;
}


/* ==========================================================
   GENERATE BUTTON
   ========================================================== */

div.stButton > button {
    width: 100%;
    height: 50px;

    border-radius: 12px;
    border: none;

    background:
        linear-gradient(
            90deg,
            #7c5cff,
            #c14cff,
            #ff4ecd
        );

    color: white;

    font-size: 16px;
    font-weight: 700;

    transition: all 0.2s ease;
}


div.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 8px 25px rgba(193, 76, 255, 0.35);
}


/* ==========================================================
   OVERVIEW CARD
   ========================================================== */

.overview-card {
    padding: 25px;

    border-radius: 20px;

    background:
        linear-gradient(
            135deg,
            rgba(55, 48, 100, 0.55),
            rgba(24, 27, 39, 0.95)
        );

    border: 1px solid rgba(139,124,255,0.25);

    line-height: 1.8;

    color: #dfe3eb;

    margin-bottom: 25px;
}


/* ==========================================================
   DAY CARD
   ========================================================== */

.day-card {
    padding: 25px;

    border-radius: 20px;

    background: #11141c;

    border: 1px solid #292e3a;

    margin-bottom: 18px;

    box-shadow:
        0 8px 30px rgba(0,0,0,0.20);
}


.day-title {
    font-size: 24px;
    font-weight: 750;

    color: #ffffff;

    margin-bottom: 18px;
}


.time-title {
    font-weight: 700;
    color: #a78bfa;

    margin-bottom: 5px;
}


.day-text {
    color: #c9ced8;

    line-height: 1.7;

    margin-bottom: 15px;
}


/* ==========================================================
   INFORMATION CARDS
   ========================================================== */

.info-card {
    padding: 22px;

    border-radius: 18px;

    background: #11141c;

    border: 1px solid #292e3a;

    min-height: 180px;
}


.info-title {
    font-size: 20px;
    font-weight: 750;

    color: #ffffff;

    margin-bottom: 12px;
}


.info-text {
    color: #c9ced8;

    line-height: 1.7;
}


/* ==========================================================
   LISTS
   ========================================================== */

.custom-list {
    color: #c9ced8;

    line-height: 1.8;

    padding-left: 20px;
}


.custom-list li {
    margin-bottom: 8px;
}


/* ==========================================================
   FOOTER
   ========================================================== */

.footer {
    text-align: center;

    color: #777f8f;

    margin-top: 50px;

    padding-top: 25px;

    border-top: 1px solid #242832;

    font-size: 14px;
}


/* ==========================================================
   MOBILE RESPONSIVE
   ========================================================== */

@media (max-width: 768px) {

    .hero-title {
        font-size: 34px;
    }

    .hero-subtitle {
        font-size: 15px;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

}

/* Remove Streamlit top header */
header[data-testid="stHeader"] {
    display: none !important;
}

/* Remove the extra top gap after hiding header */
.stAppViewContainer {
    padding-top: 0 !important;
}

.main .block-container {
    padding-top: 0 !important;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# 8. HERO SECTION
# ============================================================

st.markdown(
    """
<div class="hero">
<div class="hero-title">✈️ AI Travel Planner</div>
<div class="hero-subtitle">
Plan smarter. Explore better. Travel with confidence.<br>
Powered by LangChain + Google Gemini.
</div>
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# 9. TRIP INPUT SECTION
# ============================================================

st.markdown(
    '<div class="section-title">🧳 Plan Your Trip</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="input-card">',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


with col1:

    destination = st.text_input(
        "📍 Destination",
        placeholder="Example: Hyderabad"
    )

    budget = st.number_input(
        "💰 Budget (₹)",
        min_value=1,
        value=15000,
        step=1000
    )


with col2:

    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        max_value=30,
        value=3,
        step=1
    )

    interests = st.text_input(
        "🎯 Interests",
        placeholder="Food, history, shopping, photography"
    )


st.markdown("<br>", unsafe_allow_html=True)


generate = st.button(
    "✈️ Generate / Regenerate Travel Plan"
)


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 10. GENERATE TRAVEL PLAN
# ============================================================

if generate:

    if not destination or not interests:

        st.warning(
            "⚠️ Please enter both destination and interests."
        )

    else:

        with st.spinner(
            "✨ Creating your personalized travel plan..."
        ):

            try:

                result = travel_chain.invoke({
                    "destination": destination,
                    "budget": budget,
                    "days": days,
                    "interests": interests,
                    "format_instructions":
                        parser.get_format_instructions()
                })


                # ==================================================
                # DESTINATION OVERVIEW
                # ==================================================

                st.markdown(
                    '<div class="section-title">📍 Destination Overview</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
<div class="overview-card">
{result.destination_overview}
</div>
""",
                    unsafe_allow_html=True
                )


                # ==================================================
                # DAY-WISE ITINERARY
                # ==================================================

                st.markdown(
                    '<div class="section-title">📅 Day-wise Itinerary</div>',
                    unsafe_allow_html=True
                )


                for day in result.itinerary:

                    food_html = "".join(
                        f"<li>{food}</li>"
                        for food in day.food_suggestions
                    )

                    st.markdown(
                        f"""
<div class="day-card">

<div class="day-title">
🗓️ Day {day.day}
</div>

<div class="time-title">
🌅 Morning
</div>

<div class="day-text">
{day.morning}
</div>

<div class="time-title">
☀️ Afternoon
</div>

<div class="day-text">
{day.afternoon}
</div>

<div class="time-title">
🌆 Evening
</div>

<div class="day-text">
{day.evening}
</div>

<div class="time-title">
🍴 Food Suggestions
</div>

<ul class="custom-list">
{food_html}
</ul>

</div>
""",
                        unsafe_allow_html=True
                    )


                # ==================================================
                # TRIP SUMMARY
                # ==================================================

                st.markdown(
                    '<div class="section-title">💡 Trip Summary</div>',
                    unsafe_allow_html=True
                )


                # ==================================================
                # BUDGET
                # ==================================================

                col1, col2 = st.columns(2)


                with col1:

                    st.markdown(
                        f"""
<div class="info-card">

<div class="info-title">
💰 Estimated Budget
</div>

<div class="info-text">
{result.estimated_budget}
</div>

</div>
""",
                        unsafe_allow_html=True
                    )


                # ==================================================
                # ACTIVITIES
                # ==================================================

                with col2:

                    activities_html = "".join(
                        f"<li>{activity}</li>"
                        for activity in result.activities
                    )

                    st.markdown(
                        f"""
<div class="info-card">

<div class="info-title">
🎯 Activities
</div>

<ul class="custom-list">
{activities_html}
</ul>

</div>
""",
                        unsafe_allow_html=True
                    )


                st.markdown("<br>", unsafe_allow_html=True)


                # ==================================================
                # FOOD SUGGESTIONS
                # ==================================================

                col1, col2 = st.columns(2)


                with col1:

                    food_html = "".join(
                        f"<li>{food}</li>"
                        for food in result.food_suggestions
                    )

                    st.markdown(
                        f"""
<div class="info-card">

<div class="info-title">
🍴 Food Suggestions
</div>

<ul class="custom-list">
{food_html}
</ul>

</div>
""",
                        unsafe_allow_html=True
                    )


                # ==================================================
                # TRAVEL TIPS
                # ==================================================

                with col2:

                    tips_html = "".join(
                        f"<li>{tip}</li>"
                        for tip in result.travel_tips
                    )

                    st.markdown(
                        f"""
<div class="info-card">

<div class="info-title">
💡 Travel Tips
</div>

<ul class="custom-list">
{tips_html}
</ul>

</div>
""",
                        unsafe_allow_html=True
                    )


                # ==================================================
                # FOOTER
                # ==================================================

                st.markdown(
                    """
<div class="footer">
✈️ AI Travel Planner
<br>
Built with Python · LangChain · Google Gemini · Streamlit
</div>
""",
                    unsafe_allow_html=True
                )


            except Exception as e:

                st.error(
                    f"❌ Something went wrong: {e}"
                )