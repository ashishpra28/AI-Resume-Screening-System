import streamlit as st
from utils import extract_text_from_pdf, preprocess_text, calculate_similarity

st.title("🧾AI Resume Screening System")

st.write("Upload resumes and compare them with the job description.")

# Job description input
job_description = st.text_area("Enter Job Description")

# Resume upload
uploaded_files = st.file_uploader(
    "Upload Resumes (PDF)",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files and job_description:

    resume_texts = []
    resume_names = []

    for file in uploaded_files:

        text = extract_text_from_pdf(file)

        cleaned_text = preprocess_text(text)

        resume_texts.append(cleaned_text)

        resume_names.append(file.name)

    cleaned_job_description = preprocess_text(job_description)

    scores = calculate_similarity(resume_texts, cleaned_job_description)

    results = list(zip(resume_names, scores))

    results = sorted(results, key=lambda x: x[1], reverse=True)

    st.subheader("Resume Ranking")

    import pandas as pd

results_df = pd.DataFrame(results, columns=["Resume", "Similarity Score"])

results_df["Similarity Score"] = results_df["Similarity Score"] * 100

results_df = results_df.sort_values(by="Similarity Score", ascending=False)

results_df["Rank"] = range(1, len(results_df) + 1)

results_df = results_df[["Rank", "Resume", "Similarity Score"]]

st.dataframe(results_df)