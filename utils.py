import PyPDF2

def extract_text_from_pdf(file):
    text = ""
    
    pdf_reader = PyPDF2.PdfReader(file)
    
    for page in pdf_reader.pages:
        text += page.extract_text()
        
    return text

import re
import nltk
from nltk.corpus import stopwords

# download stopwords once
nltk.download('stopwords')

def preprocess_text(text):
    
    text = text.lower()
    
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    
    words = text.split()
    
    stop_words = set(stopwords.words('english'))
    
    filtered_words = [word for word in words if word not in stop_words]
    
    cleaned_text = " ".join(filtered_words)
    
    return cleaned_text

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resumes, job_description):

    documents = resumes + [job_description]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    return similarity_scores.flatten()

