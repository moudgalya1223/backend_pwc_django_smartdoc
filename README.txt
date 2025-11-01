
SmartDoc — Intelligent Document Search & Recommendation System
==============================================================

Overview
--------
SmartDoc is a Django-based web application that allows users to upload documents (PDF, Word, CSV, TXT, etc.)
and then perform semantic search and recommendations using AI-powered embeddings.

It extracts text from uploaded files, generates vector embeddings using SentenceTransformer, and stores them
in a Vector Database (Qdrant) for fast similarity search.

Tech Stack
----------
Layer             | Technology                  | Purpose
------------------|-----------------------------|------------------------------------
Backend           | Django + Django REST Framework | Core API and business logic
AI/ML             | Sentence Transformers (all-MiniLM-L6-v2) | Generate semantic embeddings
Data Processing   | Pandas, NumPy, pdfplumber, python-docx | Extract text from documents
Vector Database   | Qdrant                       | Store and search embeddings efficiently
Frontend (future) | Angular                      | Upload and search interface

Project Structure
-----------------
smartdoc/
├── api/
│   ├── models.py               # Document model
│   ├── views.py                # Upload, Recommend endpoints
│   ├── admin.py                # Admin registration
├── services/
│   ├── document_service.py     # Extract text from uploaded files
│   ├── embedding_service.py    # Generate vector embeddings
│   ├── storage_service.py      # Save metadata + embeddings to DB + Qdrant
│   ├── recommendation_service.py # Recommend similar documents
├── smartdoc/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── venv/                       # Virtual environment (local)
└── requirements.txt

Getting Started
---------------
1. Clone the Repository
   git clone https://github.com/yourusername/smartdoc.git
   cd smartdoc

2. Create Virtual Environment
   python -m venv venv
   venv\Scripts\activate  (Windows)
   source venv/bin/activate (macOS/Linux)

3. Install Dependencies
   pip install -r requirements.txt

4. Run Qdrant (Vector DB)
   docker run -p 6333:6333 qdrant/qdrant

5. Run Django Migrations
   python manage.py makemigrations
   python manage.py migrate

6. Start Server
   python manage.py runserver

7. Access App
   http://127.0.0.1:8000/

License
-------
This project is for educational and enterprise prototyping purposes.
