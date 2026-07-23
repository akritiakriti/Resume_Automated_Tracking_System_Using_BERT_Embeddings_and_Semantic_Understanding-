# Resume_Automated_Tracking_System_Using_BERT_Embeddings_and_Semantic_Understanding-

# ATS Resume Scorer - AI Powered Resume Analysis System

An AI-powered Applicant Tracking System (ATS) that analyzes resumes against job descriptions using Natural Language Processing (NLP) and transformer-based models. The system evaluates resume compatibility, generates ATS scores, identifies missing skills, and provides personalized recommendations to improve resume quality.

---

# Project Overview

Applicant Tracking Systems (ATS) are widely used by organizations to automatically filter and rank resumes during recruitment. Many candidates fail initial screening because their resumes do not effectively match job requirements.

This project develops an intelligent ATS Resume Scoring platform that automates resume evaluation using Artificial Intelligence and Machine Learning techniques. The system extracts resume information, compares it with job descriptions, calculates compatibility scores, identifies missing skills, and generates improvement recommendations.

The platform integrates document processing, NLP-based semantic analysis, machine learning models, and automated report generation to provide a complete resume evaluation workflow.

---

# Features

## Resume Upload & Processing

- Supports PDF, DOC, and DOCX resume formats
- Performs file validation
- Extracts text from uploaded resumes
- Cleans and preprocesses extracted content

## AI-Based Resume Analysis

- Uses transformer-based NLP models for semantic understanding
- Generates contextual embeddings using BERT/Sentence Transformer models
- Performs resume and job description similarity analysis
- Evaluates resume relevance based on:
  - Skills
  - Keywords
  - Experience
  - Resume structure
  - Job requirements

## ATS Scoring Engine

Generates an ATS compatibility score based on multiple evaluation factors:

- Overall Resume Score
- Keyword Match Score
- Skill Match Analysis
- Resume Formatting Score
- Experience Relevance Score

## Recommendation Engine

Provides:

- Missing keyword identification
- Missing skill detection
- Resume improvement suggestions
- Job-specific feedback

## Automated Report Generation

- Generates ATS evaluation reports
- Provides score breakdown
- Displays recommendations
- Exports analysis results into PDF format

---

# System Architecture

```
              Resume Upload
                    |
                    |
              File Validation
                    |
                    |
          Resume Text Extraction
          (PDF / DOC / DOCX)
                    |
                    |
          Text Preprocessing
                    |
                    |
      BERT / Sentence Transformer Model
                    |
                    |
          ATS Evaluation Engine
                    |
        +-----------+-----------+
        |           |           |
        |           |           |
    Scoring     Keyword   Recommendation
    Engine      Matching      Engine
                    |
                    |
          PDF Report Generation
```

---

# Technologies Used

## Programming Language

- Python

## Backend

- FastAPI
- Uvicorn
- REST API

## Machine Learning & NLP

- BERT
- Sentence Transformers
- HuggingFace Transformers
- spaCy
- Scikit-learn
- NumPy
- Pandas

## Frontend

- Streamlit

## Database & Authentication

- PostgreSQL
- Supabase Authentication

## Development & Deployment

- Docker
- Git
- GitHub

---

# Project Structure

```
ATS-Resume-Scorer/

│
├── backend/
│   ├── main.py
│   ├── services/
│   ├── models/
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py
│   └── components/
│
├── notebook/
│   └── model_training.ipynb
│
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Machine Learning Pipeline

The AI evaluation pipeline follows these steps:

1. Resume and Job Description Input
2. Document Text Extraction
3. Text Cleaning and Preprocessing
4. Feature Extraction using Transformer Embeddings
5. Semantic Similarity Calculation
6. ATS Score Generation
7. Missing Skill and Keyword Detection
8. Recommendation Generation
9. PDF Report Creation

---

# Data Privacy & Security

- Resume analysis is performed locally within the application environment.
- Candidate resumes are not sent to external AI APIs.
- Sensitive resume information remains protected during processing.
- Authentication and database access are managed securely using Supabase.

---

# Evaluation Output

The system provides:

- ATS Compatibility Score
- Resume Strength Analysis
- Missing Skills
- Missing Keywords
- Improvement Recommendations
- Downloadable PDF Report

---

# Future Improvements

- Improve scoring accuracy with larger labeled datasets
- Add recruiter dashboard
- Support multiple candidate ranking
- Add multilingual resume analysis
- Deploy using cloud infrastructure
- Integrate advanced LLM-based feedback generation

---


# Acknowledgements

- HuggingFace Transformers
- Sentence Transformers
- spaCy NLP Library
- FastAPI
- Streamlit
- Supabase