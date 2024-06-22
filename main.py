import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-1.5-flash')


def get_response_tex(resume,information,jd):
    prompt=f"""

    Act as an experienced Application Tracking System (ATS) with expertise in the tech field, including software engineering, data science, data analysis, and big data engineering. Your job is to accept a template LaTeX code for a resume from the Candidate along with Job Description and Candidate's personal infromation. Based on the job description and Candidate's information, you populate the template latex code and generate a resume in tex format for the Candidate.  Assess the job description and populate the resume with right keywords, that is optimized for ATS Scanner with respect to the provided Job Description

    Here is the LaTeX code for template resume: {resume}
    Here is the Candidate's information: {information}
    Here is the job description: {jd}

    Only respond with the LaTeX code and nothing else. 
    """

    response = model.generate_content(prompt)
    return response.text

def get_response_markdown(information,jd):
    prompt=f"""
    Act as an experienced Application Tracking System (ATS) with expertise in the tech field, including software engineering, data science, data analysis, and big data engineering. Your job is to accept a Job Description and Candidate's personal infromation. Based on the job description and Candidate's information, you generate a resume in markdown code format for the Candidate.  Assess the job description and populate the resume with right keywords, that is optimized for ATS Scanner with respect to the provided Job Description.

    Here is the Candidate's information: {information}
    Here is the job description: {jd}

    Only respond with the markdown code for resume and nothing else. 
    """
    response = model.generate_content(prompt)
    return response.text
    

#streamlit app
st.title("🔗Resume Copilot")
st.subheader("Get ATS optimized Resume at the speed of AI")
jd = st.text_area("Enter the Job Description:")
info = st.text_area("Enter the Candidate's Information:")
res = st.text_area("Enter LaTeX resume template:")


if st.button("Generate TeX Resume"):
    if jd and info and res:
        resp=get_response_tex(res,info,jd)
        st.text_area("Here's your TeX Resume:", value=resp, height=600)
    else:
        st.warning("Please enter both Job Description and Candidate's Information.")

if st.button("Generate Markdown Resume"):
    if jd and info and not res:
        resp=get_response_markdown(info, jd)
        st.text_area("Here's your Markdown Resume:", value=resp, height=600)
    else:
        st.warning("Please enter both Job Description and Candidate's Information.")

st.subheader("The program above outputs code in either TeX or Markdown, which you can then modify to suit your needs.")