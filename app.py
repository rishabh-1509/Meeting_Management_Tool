import streamlit as st
import tempfile

from document_utils import process_uploaded_files, store_document_embeddings
from clustering import cluster_discussion_topics
from gpt_summary import generate_gpt4_summary, generate_detailed_summary
from video_utils import transcribe_video, analyze_discussion_topics
from chromadb_utils import retrieve_relevant_information
import moviepy.editor as mp


# Streamlit app
st.title("Pre-Meeting Document and Video Management")

# Document upload and discussion topics
uploaded_files = st.file_uploader("Upload relevant documents", accept_multiple_files=True, type=["txt", "pdf"])
documents = process_uploaded_files(uploaded_files)

# Store document embeddings for RAG retrieval
if documents:
    store_document_embeddings(documents)

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
    clustered_data = cluster_discussion_topics(discussion_data)

    st.subheader("Clustered Discussion Topics")
    for cluster_id, topics in clustered_data.items():
        st.write(f"**Cluster {cluster_id + 1}:**")
        for topic in topics:
            st.write(f"- {topic}")

    # Generate meeting agenda using GPT-4
    st.subheader("Meeting Agenda")
    for cluster_id, topics in clustered_data.items():
        context = "\n".join(topics)
        agenda = generate_gpt4_summary(f"Clustered Topics: {context}\nGenerate a short agenda (2 lines).")
        st.write(f"**Cluster {cluster_id + 1} Agenda:** {agenda}")

# Video upload section
st.subheader("Upload a Meeting Video")
uploaded_video = st.file_uploader("Upload a meeting video", type=["mp4", "avi", "mkv"])

# Video transcription and analysis
if uploaded_video is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
        temp_file.write(uploaded_video.read())
        video_path = temp_file.name

    video_clip = mp.VideoFileClip(video_path)
    audio_path = video_path.replace(".mp4", ".mp3")
    video_clip.audio.write_audiofile(audio_path)

    transcription = transcribe_video(audio_path)
    st.subheader("Video Transcription")
    st.write(transcription)

    # Analyze discussion topics in video
    covered_topics, unresolved_topics = analyze_discussion_topics(transcription, discussion_data)

    if covered_topics:
        st.write("### Covered Discussion Topics:")
        for topic in covered_topics:
            st.write(f"- {topic}")

    if unresolved_topics:
        st.write("### Unresolved Discussion Topics:")
        for topic in unresolved_topics:
            st.write(f"- {topic}")

    # Generate detailed meeting summary using GPT-4
    st.subheader("Detailed Meeting Summary")
    detailed_summary = generate_detailed_summary(transcription, discussion_data, "Decisions made", "Action items assigned")
    st.write(detailed_summary)

# Add "Retrieve Relevant Information" button
if st.button("Retrieve Relevant Information"):
    st.subheader("Relevant Information from Uploaded Documents")
    for topic in discussion_data:
        relevant_docs = retrieve_relevant_information(topic, documents)
        st.write(f"**Topic: {topic}**")
        for doc in relevant_docs:
            st.write(f"- {doc[:200]}...")  # Displaying a short snippet of each relevant document
