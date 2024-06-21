
# Resume Copilot

## Description
Resume Copilot is a tool that leverages Google's Gemini-Pro model to assist in creating ATS (Application Tracking System) optimized resumes. It takes a LaTeX template for a resume, a job description, and candidate information as input and generates a populated resume template in LaTeX format.

## Installation
1. Clone the repository.
2. Install the required dependencies listed in `requirements.txt` using `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory of the project and populate it with your `GOOGLE_API_KEY`.

## Usage
1. Run the Streamlit app using `streamlit run app.py`.
2. Enter the job description, candidate's information, and the LaTeX resume template into the respective text areas.
3. Click the "Generate Resume" button to generate the populated resume template.
4. The populated resume template will be displayed in the app.

## Deployment
The app is deployed and can be accessed at [https://resumewiser.streamlit.app/](https://resumewiser.streamlit.app/).

