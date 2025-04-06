DocuVille Software Engineer Technical Assessment 2025

Problem Statement

Create a document similarity detection system that compares two text documents and returns a similarity score between 0 and 1.

System Design 

Components:

Input Layer: Accept two text files (doc1.txt, doc2.txt)

Preprocessing: Lowercase, remove punctuation and stopwords

Feature Extraction: TF-IDF Vectorization

Similarity Calculation: Cosine Similarity

Output: Print similarity score

Design Diagram:

doc1.txt ──┐
           ├─> Preprocessing ──> TF-IDF Vectorizer ──┐
doc2.txt ──┘                                          │
                                        Cosine Similarity ──> Similarity Score

Files

doc1.txt: Contains first document text

doc2.txt: Contains second document text

doc_similarity.py: Python script that calculates similarity score

How to Run

Make sure you have Python 3.7+

Install dependencies:

pip install scikit-learn nltk

Run the script:

python doc_similarity.py

Output will be like:

Similarity Score: 0.2882

Sample Inputs

doc1.txt:

Artificial intelligence is transforming the world. It is used in automation, healthcare, and finance.

doc2.txt:

AI is changing how the world works. It has applications in healthcare, automation, and financial sectors.

Feedback

This task was a great hands-on experience in text similarity and NLP.

TF-IDF and cosine similarity made for a simple yet effective baseline solution.

Improvements If More Time Was Available

Use semantic similarity (Sentence Transformers / BERT)

Compare more than 2 documents at once

Build a web UI with drag-and-drop features

Use vector storage for efficient large-scale comparisons

Screenshot of Output



GitHub Repo (Optional): [Add your GitHub repo link here]

Screenshots / Proof of Work: Included above as similarity_output_screenshot.png

