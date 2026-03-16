# 📄 AI Resume Screening System

An **AI-powered NLP project** that automatically ranks resumes based on how well they match a given job description using **TF-IDF Vectorization** and **Cosine Similarity**, deployed through an interactive **Streamlit web application**.

---

# 🚀 Project Overview

Recruiters often receive **hundreds of resumes** for a single job role.  
Manually screening them is time-consuming and inefficient.

This project automates the **initial resume screening process** by comparing uploaded resumes with a job description and ranking them based on relevance.

Users can:
- Upload multiple resumes in **PDF format**
- Enter a **job description**
- Instantly see **ranked candidates based on similarity score**

---

# 🧠 Problem Statement

Recruitment teams need a faster way to identify candidates whose skills match job requirements.

The objective of this project is to build a **resume ranking system** that:

1. Extracts text from resumes  
2. Processes and cleans the text using NLP  
3. Converts text into numerical vectors  
4. Measures similarity between resumes and job description  
5. Ranks candidates based on relevance  

This simulates the **basic working principle of Applicant Tracking Systems (ATS)** used in modern recruitment.

---

# 📂 Project Structure

```
AI-Resume-Screening-System
│
├── notebook
│   └── resume_screening.ipynb
│
├── data
│   └── resumes
│
├── utils.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Tech Stack

| Category | Tools Used |
|--------|-------------|
| Programming Language | Python |
| NLP Library | NLTK |
| Machine Learning | Scikit-learn |
| Feature Extraction | TF-IDF Vectorization |
| Similarity Measure | Cosine Similarity |
| Resume Parsing | PyPDF2 |
| Web Application | Streamlit |

---

# 📊 System Workflow

```
Uploaded Resumes (PDF)
        ↓
Text Extraction (PyPDF2)
        ↓
Text Preprocessing (NLTK)
(lowercase, stopword removal)
        ↓
TF-IDF Vectorization
        ↓
Cosine Similarity
        ↓
Resume Ranking
```

---

# 📈 Example Output

| Rank | Resume | Match Score |
|-----|------|------|
| 1 | resume3.pdf | 82.31% |
| 2 | resume1.pdf | 71.14% |
| 3 | resume2.pdf | 45.22% |

This helps recruiters quickly identify the **most relevant candidates**.

---

# ✨ Features

- Upload multiple resumes  
- Automatic PDF text extraction  
- NLP-based text preprocessing  
- TF-IDF feature extraction  
- Cosine similarity ranking  
- Interactive Streamlit web application  

---

# 🔮 Future Improvements

- Skill extraction using **Named Entity Recognition (NER)**
- Keyword highlighting in resumes
- Support for **DOCX resumes**
- Advanced resume parsing using **SpaCy**
- Candidate analytics dashboard
- Deployment using **Docker + AWS**

---

# 🌐 Live Application

Live App: https://ai-resume-screening-system-wm9vvjyqvdt7dfjhe9mdlj.streamlit.app/

---

⭐ If you like this project, consider giving it a **star on GitHub**.
