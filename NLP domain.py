from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import pandas as pd

# Load company names
df = pd.read_excel("Merged Data\output_with_experience.xlsx")
company_names = df["companyName"].dropna().unique().tolist()

# Get sentence embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(company_names)

# Use KMeans to group into 6 clusters
kmeans = KMeans(n_clusters=6, random_state=0)
labels = kmeans.fit_predict(embeddings)

# Assign cluster labels as domain placeholders
df["domain"] = df["companyName"].map(dict(zip(company_names, labels)))
