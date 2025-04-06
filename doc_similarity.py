import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

# Download stopwords if not already done
nltk.download('stopwords')
from nltk.corpus import stopwords

def preprocess(text):
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    filtered = [word for word in tokens if word not in stop_words]
    return " ".join(filtered)

# Load documents
with open('doc1.txt', 'r', encoding='utf-8') as f:
    doc1 = f.read()

with open('doc2.txt', 'r', encoding='utf-8') as f:
    doc2 = f.read()

# Preprocess documents
doc1_clean = preprocess(doc1)
doc2_clean = preprocess(doc2)

# Vectorize
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([doc1_clean, doc2_clean])

# Compute similarity
score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
print(f"Similarity Score: {score:.4f}")