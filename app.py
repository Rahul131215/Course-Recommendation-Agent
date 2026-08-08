import streamlit as st
from recommender import recommend_courses

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Course Recommendation Agent",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, #0b5394, #3d85c6);
    padding: 45px;
    border-radius: 25px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 50px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 20px;
    opacity: 0.95;
}

/* Glass Card */
.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* Feature Cards */
.feature {
    background: linear-gradient(145deg, #ffffff, #f0f4ff);
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    height: 100%;
}

.feature h3 {
    color: #0b5394;
}

/* Footer */
.footer {
    text-align: center;
    color: gray;
    padding: 20px;
    margin-top: 40px;
}

/* Button Styling */
div.stButton > button {
    background: linear-gradient(90deg, #0b5394, #3d85c6);
    color: white;
    font-size: 18px;
    border-radius: 14px;
    padding: 12px 20px;
    border: none;
    width: 100%;
    transition: 0.3s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    background: linear-gradient(90deg, #073763, #0b5394);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero">
    <h1>🎓 AI Course Recommendation Agent</h1>
    <p>Transform your background, skills, and career goals into a personalized AI-powered learning roadmap.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("📌 About Project")
    st.success("Built by Rahul Biradar 🚀")

    st.markdown("### 🛠️ Tech Stack")
    st.write("• Python")
    st.write("• Streamlit")
    st.write("• Groq API")
    st.write("• Llama 3.3")
    st.write("• JSON")
    st.write("• GitHub")

    st.markdown("### 💡 Tips")
    st.info("Enter **2–5 skills** for better AI recommendations.")

# ---------------- FEATURE SECTION ----------------
st.subheader("✨ What This AI Agent Does")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature">
        <h3>🎯 Personalized</h3>
        <p>Recommendations based on your unique background and goals.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature">
        <h3>⚡ Instant AI Analysis</h3>
        <p>AI analyzes your profile and creates a roadmap within seconds.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature">
        <h3>📚 Structured Learning</h3>
        <p>Step-by-step learning path with clear explanations and career benefits.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------- WORKFLOW ----------------
st.subheader("🔄 How It Works")

w1, w2, w3, w4 = st.columns(4)

w1.metric("Step 1", "Enter Profile")
w2.metric("Step 2", "AI Analysis")
w3.metric("Step 3", "Generate Roadmap")
w4.metric("Step 4", "Start Learning")

st.write("")

# ---------------- INPUT FORM ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📝 Student Profile")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 Full Name", placeholder="Rahul Biradar")
    background = st.text_input("🎓 Educational Background", placeholder="B.E Computer Science")

with col2:
    skills = st.text_input("💻 Current Skills", placeholder="Python, Java, SQL")
    goal = st.text_input("🚀 Career Goal", placeholder="Software Developer / AI Engineer / Data Analyst")

st.progress(30, text="Complete your profile for AI analysis")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- GENERATE BUTTON ----------------
if st.button("✨ Generate AI Learning Path"):

    profile = {
        "name": name,
        "background": background,
        "skills": [s.strip() for s in skills.split(",") if s.strip()],
        "goal": goal
    }

    with st.spinner("🤖 AI is analyzing your profile and preparing recommendations..."):
        result = recommend_courses(profile)

    st.balloons()

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(f"📚 Personalized Learning Path for {name}")
    st.success("AI analysis completed successfully!")
    st.markdown(result)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- BENEFITS ----------------
st.subheader("🌟 Why Use This AI Agent?")

left, right = st.columns(2)

with left:
    st.markdown("""
    ### ✅ Benefits
    - Saves time in choosing courses
    - Provides a structured learning roadmap
    - Helps focus only on relevant skills
    - Beginner-friendly interface
    - Accessible from any browser and device
    """)

with right:
    st.markdown("""
    ### 🎯 Best For
    - Students
    - Fresh Graduates
    - Career Changers
    - Self-Learners
    - Training Institutes
    """)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    Built with ❤️ using <b>Python + Streamlit + Groq Llama 3.3</b><br>
    AI Course Recommendation Agent • Rooman JARA Project • Rahul Biradar
</div>
""", unsafe_allow_html=True)
