import streamlit as st
from recommender import recommend_courses

# ---------- PAGE SETTINGS ----------
st.set_page_config(
    page_title="AI Course Recommendation Agent",
    page_icon="🎓",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #0b5394;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #555;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">🎓 AI Course Recommendation Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get a personalized AI-powered learning roadmap based on your background, skills, and career goals.</div>', unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("📌 About This Project")
    st.write("""
    This application uses **AI (Groq Llama 3.3)** to generate personalized course recommendations.

    **Technologies Used:**
    - Python
    - Streamlit
    - Groq API
    - JSON
    - GitHub
    """)

    st.success("Developed by Rahul Biradar 🚀")

# ---------- INPUT CARD ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 Full Name", placeholder="Enter your full name")
    background = st.text_input("🎓 Educational Background", placeholder="B.E Computer Science")

with col2:
    skills = st.text_input("💻 Current Skills", placeholder="Python, Java, SQL")
    goal = st.text_input("🚀 Career Goal", placeholder="AI Engineer / Software Developer / Data Analyst")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- GENERATE BUTTON ----------
if st.button("✨ Generate AI Learning Path", use_container_width=True):

    profile = {
        "name": name,
        "background": background,
        "skills": [s.strip() for s in skills.split(",") if s.strip()],
        "goal": goal
    }

    with st.spinner("🤖 AI is analyzing your profile and preparing recommendations..."):
        result = recommend_courses(profile)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(f"📚 Personalized Learning Path for {name}")
    st.markdown(result)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown('<div class="footer">Built with ❤️ using Streamlit + Groq LLM</div>', unsafe_allow_html=True)
