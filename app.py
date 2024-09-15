import openai
import streamlit as st
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import tempfile
import moviepy.editor as mp
import whisper
import chromadb
from gpt_summary import generate_gpt4_summary, generate_detailed_summary
from document_utils import process_uploaded_files
from video_utils import transcribe_video, analyze_discussion_topics
from clustering import cluster_discussion_topics

# Initialize ChromaDB client for RAG retrieval
client = chromadb.Client()

# OpenAI GPT API setup
openai.api_key = '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'

# Streamlit app
st.title("Pre-Meeting Document and Video Management")

# Document upload and processing
uploaded_files = st.file_uploader("Upload relevant documents", accept_multiple_files=True, type=["txt", "pdf"])
documents = []
if uploaded_files:
    documents = process_uploaded_files(uploaded_files)

# Store document embeddings for RAG retrieval
if documents:
    embeddings = [model.encode(doc["content"]) for doc in documents]
    client.create_collection(name="documents", embeddings=embeddings, ids=[doc["name"] for doc in documents])

discussion_data = []
with st.form(key='discussion_form'):
    participant_name = st.text_input("Your Name", "")
    discussion_topic = st.text_area("Discussion Topics")
    submit_button = st.form_submit_button(label="Submit Topics")
    if submit_button:
        if participant_name and discussion_topic:
            discussion_data.append(discussion_topic)
            st.success(f"Thank you {participant_name}, your discussion topics have been submitted!")

# Clustering discussion topics
if len(discussion_data) > 1:
    labels = cluster_discussion_topics(discussion_data)
    clustered_data = {}
    for i, label in enumerate(labels):
        if label not in clustered_data:
            clustered_data[label] = []
        clustered_data[label].append(discussion_data[i])

    st.subheader("Clustered Discussion Topics")
    for cluster_id, topics in clustered_data.items():
        st.write(f"**Cluster {cluster_id + 1}:**")
        for topic in topics:
            st.write(f"- {topic}")

    # Generate agenda from clustered topics
    st.subheader("Meeting Agenda")
    for cluster_id, topics in clustered_data.items():
        context = "\n".join(topics)
        agenda = generate_gpt4_summary(f"Based on the following clustered topics, generate a concise meeting agenda with three main points: {context}", "agenda")
        st.write(f"**Cluster {cluster_id + 1} Agenda:** {agenda}")

# Video upload section
st.subheader("Upload a Meeting Video")
uploaded_video = st.file_uploader("Upload a meeting video", type=["mp4", "avi", "mkv"])

if uploaded_video is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
        temp_file.write(uploaded_video.read())
        video_path = temp_file.name

    # Transcribe video using Whisper
    audio_path = video_path.replace(".mp4", ".mp3")
    video_clip = mp.VideoFileClip(video_path)
    video_clip.audio.write_audiofile(audio_path)
    transcription = transcribe_video(audio_path)
    st.subheader("Video Transcription")
    st.write(transcription)

    # Analyze discussion topics
    covered_topics, unresolved_topics = analyze_discussion_topics(transcription, discussion_data)
    
    st.subheader("Analysis of Discussion Topics in Video")
    if covered_topics:
        st.write("### Covered Discussion Topics:")
        for topic in covered_topics:
            st.write(f"- {topic}")
    if unresolved_topics:
        st.write("### Unresolved Discussion Topics:")
        for topic in unresolved_topics:
            st.write(f"- {topic}")

    # Generate detailed meeting summary
    st.subheader("Detailed Meeting Summary")
    detailed_summary = generate_detailed_summary(transcription, discussion_data, "Decisions made", "Action items assigned")
    st.write(detailed_summary)

if st.button("Retrieve Relevant Information"):
    st.subheader("Relevant Information from Uploaded Documents")
    for topic in discussion_data:
        query = f"Retrieve relevant information based on the discussion topic: {topic}"
        relevant_docs = retrieve_relevant_information(query, documents)
        st.write(f"**Topic: {topic}**")
        for doc in relevant_docs:
            st.write(f"- {doc[:200]}...")  # Displaying a short snippet of each relevant document
