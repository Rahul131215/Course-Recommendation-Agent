import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Please create a .env file.")

client = Groq(api_key=api_key)


def load_courses():
    with open("courses.json", "r") as f:
        return json.load(f)


def recommend_courses(profile):
    courses = load_courses()

    course_list = ""
    for course in courses:
        course_list += (
            f"- {course['name']} "
            f"(Level: {course['level']}, "
            f"Prerequisite: {course['prerequisite']})\n"
            f"Description: {course['description']}\n\n"
        )

    prompt = f"""
You are an expert AI Career Mentor.

Student Profile:
Name: {profile['name']}
Background: {profile['background']}
Skills: {", ".join(profile['skills'])}
Career Goal: {profile['goal']}

Available Courses:
{course_list}

Create a personalized learning path.

For every recommended course include:
1. Course Name
2. Why it is recommended
3. Skills gained
4. Career benefit

Use Markdown formatting.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI Career Mentor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=1024
    )

    return response.choices[0].message.content