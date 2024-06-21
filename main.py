import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-1.5-flash')


def get_respone(resume,information,jd):
    prompt=f"""

    Act as an experienced Application Tracking System (ATS) with expertise in the tech field, including software engineering, data science, data analysis, and big data engineering. Your job is to accept a template LaTeX code for a resume from the Candidate along with Job Description and Candidate's personal infromation. Based on the job description and Candidate's information, you populate the template latex code and generate a resume in tex format for the Candidate.  Assess the job description and populate the resume with right keywords.

    Here is the LaTeX code for template resume: {resume}
    Here is the Candidate's information: {information}
    Here is the job description: {jd}

    Only respond with the LaTeX code and nothing else. 
    """

    response = model.generate_content(prompt)
    return response.text

def execute_btn(template):
    if jd and info:
        resp=get_respone(template,jd,info)
        st.text_area("Here's your Resume:", value=resp, height=600)
    else:
        st.warning("Please enter both Job Description and Candidate's Information.")

#streamlit app
st.title("🔗Resume Copilot")
st.subheader("Get ATS optimized Resume at the speed of AI")
jd = st.text_area("Enter the Job Description:",height=300)
info = st.text_area("Enter the Candidate's Information:",height=300)
res = st.text_area("Enter LaTeX resume template:",height=500)

if st.button("Generate Resume"):
    execute_btn(res)

