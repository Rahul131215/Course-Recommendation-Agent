import streamlit as st
from recommender import recommend_courses

st.set_page_config(
    page_title="AI Course Recommendation Agent",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Course Recommendation Agent")
st.write("Get a personalized AI-generated learning path.")

name = st.text_input("Name")
background = st.text_input("Educational Background")
skills = st.text_input("Skills (comma separated)")
goal = st.text_input("Career Goal")

if st.button("Generate AI Learning Path"):

    profile = {
        "name": name,
        "background": background,
        "skills": [s.strip() for s in skills.split(",") if s.strip()],
        "goal": goal
    }

    with st.spinner("Generating recommendations using AI..."):
        result = recommend_courses(profile)

    st.markdown(result)
