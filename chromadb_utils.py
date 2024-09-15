import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client()

def store_document_embeddings(documents):
    if "documents" in [collection.name for collection in client.list_collections()]:
        collection = client.get_collection(name="documents")
    else:
        collection = client.create_collection(name="documents")

    for i, doc in enumerate(documents):
        embedding = model.encode(doc["content"]).tolist()
        collection.add(
            ids=[f"doc_{i}"],
            documents=[doc["content"]],
            metadatas=[{"name": doc["name"]}],
            embeddings=[embedding]
        )

def retrieve_relevant_information(query, documents):
    query_embedding = model.encode(query)
    doc_embeddings = [model.encode(doc["content"]) for doc in documents]
    similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
    relevant_docs = sorted(zip(similarities, documents), reverse=True, key=lambda x: x[0])
    top_docs = [doc[1]["content"] for doc in relevant_docs[:3]]
    return top_docs
