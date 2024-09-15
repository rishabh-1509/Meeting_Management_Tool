# Meeting Document and Video Management System

## Overview

This project is a Streamlit-based web application designed to manage and document meetings using advanced AI technologies. The app processes uploaded documents and videos, clusters discussion topics, and generates summaries using OpenAI's GPT-4. It also utilizes ChromaDB for semantic retrieval of relevant information from documents.

## Project Structure

```
.
├── app.py              # Main Streamlit app file
├── gpt_summary.py      # OpenAI GPT-4 related functions
├── chromadb_utils.py   # ChromaDB-related utilities
├── document_utils.py   # Document upload and processing functions
├── clustering.py       # Clustering and discussion topic utilities
├── video_utils.py      # Video transcription and analysis utilities
└── requirements.txt    # Dependencies
```

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## File Descriptions

### `app.py`

This is the main entry point for the Streamlit application. It orchestrates the user interface and connects various functionalities:

- **Document Upload and Processing:** Handles the uploading of documents, processes them to extract text, and stores embeddings for retrieval.
- **Discussion Topics:** Collects discussion topics from the user, clusters them, and generates a meeting agenda using GPT-4.
- **Video Upload and Transcription:** Manages video uploads, transcribes audio to text, and analyzes the transcription for covered and unresolved discussion topics.
- **Retrieve Relevant Information:** Retrieves and displays relevant information from uploaded documents based on discussion topics.

### `gpt_summary.py`

Contains functions to interact with OpenAI's GPT-4 API to generate text summaries and meeting agendas:

- **`generate_gpt4_summary(context)`**
  - **Purpose:** Generates a summary or agenda from a given context using GPT-4.
  - **Parameters:** `context` – A string containing the information to be summarized.
  - **Returns:** A summary or agenda text.

- **`generate_detailed_summary(transcription, discussion_topics, decisions, action_items)`**
  - **Purpose:** Generates a detailed meeting summary based on transcription, discussion topics, decisions made, and action items.
  - **Parameters:** 
    - `transcription` – Text from the video transcription.
    - `discussion_topics` – List of discussion topics.
    - `decisions` – Summary of decisions made.
    - `action_items` – List of action items.
  - **Returns:** A detailed summary text.

### `chromadb_utils.py`

Handles interactions with ChromaDB for storing and retrieving document embeddings:

- **`store_document_embeddings(documents)`**
  - **Purpose:** Stores the embeddings of documents in a ChromaDB collection.
  - **Parameters:** 
    - `documents` – List of document dictionaries, each containing a `"name"` and `"content"`.
  - **Behavior:** Creates a new collection if it does not exist or updates an existing collection with the document embeddings.

- **`retrieve_relevant_information(query, documents)`**
  - **Purpose:** Retrieves relevant information from documents based on a query.
  - **Parameters:** 
    - `query` – The search query string.
    - `documents` – List of document dictionaries.
  - **Returns:** A list of the top 3 most similar documents' content.

### `document_utils.py`

Provides utilities for processing uploaded documents:

- **`process_uploaded_files(uploaded_files)`**
  - **Purpose:** Processes uploaded files to extract text from PDFs and decode text files.
  - **Parameters:** 
    - `uploaded_files` – List of uploaded files.
  - **Returns:** A list of document dictionaries with `"name"` and `"content"`.

### `clustering.py`

Contains clustering functions to group discussion topics:

- **`cluster_discussion_topics(discussion_data)`**
  - **Purpose:** Clusters discussion topics into groups using KMeans clustering.
  - **Parameters:** 
    - `discussion_data` – List of discussion topics.
  - **Returns:** A dictionary where keys are cluster IDs and values are lists of topics in that cluster.

### `video_utils.py`

Handles video transcription and analysis of discussion topics:

- **`transcribe_video(audio_path)`**
  - **Purpose:** Transcribes audio from a video file using Whisper.
  - **Parameters:** 
    - `audio_path` – Path to the audio file.
  - **Returns:** Transcription text.

- **`analyze_discussion_topics(transcription, discussion_data)`**
  - **Purpose:** Analyzes the video transcription to determine which discussion topics were covered or unresolved.
  - **Parameters:** 
    - `transcription` – Text from the video transcription.
    - `discussion_data` – List of discussion topics.
  - **Returns:** Two lists – `covered_topics` and `unresolved_topics`.

## How Components Interact

1. **User Interaction:** 
   - Users upload documents and videos through the Streamlit interface in `app.py`.
   - Discussion topics are submitted by users.

2. **Document Processing:**
   - Uploaded documents are processed by `process_uploaded_files` in `document_utils.py` to extract text.
   - Document embeddings are stored in ChromaDB using `store_document_embeddings` from `chromadb_utils.py`.

3. **Discussion Topic Clustering:**
   - Submitted discussion topics are clustered by `cluster_discussion_topics` in `clustering.py`.
   - The clustered topics are used to generate meeting agendas with `generate_gpt4_summary` in `gpt_summary.py`.

4. **Video Transcription and Analysis:**
   - Uploaded videos are processed to extract audio and transcribe it using `transcribe_video` in `video_utils.py`.
   - The transcription is analyzed to match discussion topics with `analyze_discussion_topics` in `video_utils.py`.

5. **Information Retrieval:**
   - Users can retrieve relevant information from documents based on discussion topics using `retrieve_relevant_information` from `chromadb_utils.py`.

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Upload Documents and Videos:**
   - Upload text and PDF documents.
   - Upload video files for transcription.

3. **Submit Discussion Topics:**
   - Enter and submit discussion topics via the Streamlit interface.

4. **View Results:**
   - View clustered discussion topics and meeting agenda.
   - Review video transcription and analyze discussion topics.
   - Retrieve relevant information from uploaded documents.

## Dependencies

Ensure all dependencies are installed by running:

```bash
pip install -r requirements.txt
```
