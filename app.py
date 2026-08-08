import streamlit as st
from recommender import recommend_courses

# ---------- PAGE CONFIG ----------
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

.hero {
    background: linear-gradient(135deg, #0b5394, #6fa8dc);
    padding: 40px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 48px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 20px;
    opacity: 0.95;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.feature {
    background: #ffffff;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 3px 10px rgba(0,0,0,0.06);
    height: 100%;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
    padding: 20px;
}

div.stButton > button {
    background: linear-gradient(90deg, #0b5394, #3d85c6);
    color: white;
    font-size: 18px;
    border-radius: 12px;
    padding: 12px 24px;
    border: none;
    width: 100%;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #073763, #0b5394);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
st.markdown("""
<div class="hero">
    <h1>🎓 AI Course Recommendation Agent</h1>
    <p>An intelligent AI mentor that transforms your background, skills, and career goal into a personalized learning roadmap.</p>
</div>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("📌 Project Information")

    st.success("Built by Rahul Biradar 🚀")

    st.markdown("### 🛠️ Technologies")
    st.write("• Python")
    st.write("• Streamlit")
    st.write("• Groq API")
    st.write("• Llama 3.3")
    st.write("• JSON")

    st.markdown("### 💡 AI Tips")
    st.info("Enter at least **2–3 skills** for better recommendations.")

# ---------- FEATURE CARDS ----------
st.subheader("✨ What This AI Agent Can Do")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature">
        <h3>🎯 Personalized</h3>
        <p>Recommendations based on your unique profile.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature">
        <h3>⚡ Instant AI Analysis</h3>
        <p>Get your learning roadmap within seconds.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature">
        <h3>📚 Step-by-Step Roadmap</h3>
        <p>Clear ordered learning path with explanations.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------- WORKFLOW ----------
st.subheader("🔄 How It Works")

w1, w2, w3, w4 = st.columns(4)

w1.metric("Step 1", "Enter Profile")
w2.metric("Step 2", "AI Analyzes")
w3.metric("Step 3", "Generate Roadmap")
w4.metric("Step 4", "Start Learning")

st.write("")

# ---------- INPUT FORM ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📝 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 Full Name", placeholder="Rahul Biradar")
    background = st.text_input("🎓 Educational Background", placeholder="B.E Computer Science")

with col2:
    skills = st.text_input("💻 Current Skills", placeholder="Python, Java, SQL")
    goal = st.text_input("🚀 Career Goal", placeholder="Software Developer / AI Engineer / Data Analyst")

st.progress(25, text="Complete your profile for AI analysis")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- GENERATE BUTTON ----------
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

# ---------- WHY USE THIS APP ----------
st.subheader("🌟 Why Use This AI Agent?")

left, right = st.columns(2)

with left:
    st.markdown("""
    ### ✅ Benefits
    - Saves time in choosing courses
    - Provides a structured roadmap
    - Beginner friendly
    - Accessible from any browser
    - Personalized guidance for every student
    """)

with right:
    st.markdown("""
    ### 🎯 Best For
    - Students
    - Fresh Graduates
    - Career Changers
    - Self-learners
    - Training Institutes
    """)

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    Built with ❤️ using <b>Python + Streamlit + Groq Llama 3.3</b><br>
    AI Course Recommendation Agent • Rooman JARA Project • Rahul Biradar
</div>
""", unsafe_allow_html=True)