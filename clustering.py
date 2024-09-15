from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def cluster_discussion_topics(discussion_data):
    discussion_embeddings = model.encode(discussion_data)
    num_clusters = min(5, len(discussion_data))
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(discussion_embeddings)
    labels = kmeans.labels_

    clustered_data = {}
    for i, label in enumerate(labels):
        if label not in clustered_data:
            clustered_data[label] = []
        clustered_data[label].append(discussion_data[i])
    
    return clustered_data
