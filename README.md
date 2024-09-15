# Meeting Document and Video Management System

## Overview

The Meeting Document and Video Management System is a web application built using Streamlit and various AI technologies to manage and document meetings. The system processes uploaded documents and videos, clusters discussion topics, generates meeting summaries using OpenAI's GPT-4, and performs semantic search using ChromaDB.

## Features

- **Document Upload:** Supports text and PDF file uploads.
- **Video Processing:** Transcribes meeting videos to text.
- **Discussion Topic Management:** Clusters discussion topics and generates agendas.
- **Information Retrieval:** Retrieves relevant information from documents based on discussion topics.

## Assumptions

1. **User Access:** Users have access to a computer with a web browser to interact with the Streamlit application.
2. **File Formats:** Uploaded files are assumed to be in supported formats (TXT, PDF for documents; MP4, AVI, MKV for videos).
3. **API Keys:** OpenAI and ChromaDB API keys are correctly configured and valid.
4. **Environment:** The system is assumed to run in a Python environment with necessary packages installed.

## Design and Implementation Choices

1. **Streamlit for UI:**
   - **Reasoning:** Streamlit provides an easy-to-use framework for building interactive web applications with minimal setup.
   - **Choice:** Used Streamlit for the user interface to allow users to upload files and view results interactively.

2. **OpenAI GPT-4:**
   - **Reasoning:** GPT-4 is used for generating summaries and meeting agendas due to its advanced language understanding and generation capabilities.
   - **Choice:** Integrated GPT-4 for generating detailed meeting summaries and concise agendas based on clustered discussion topics.

3. **ChromaDB:**
   - **Reasoning:** ChromaDB is utilized for semantic search and information retrieval to handle large amounts of document embeddings efficiently.
   - **Choice:** Used ChromaDB for storing document embeddings and performing similarity searches.

4. **Clustering with KMeans:**
   - **Reasoning:** KMeans clustering helps in grouping similar discussion topics, making it easier to generate an agenda.
   - **Choice:** Applied KMeans for clustering discussion topics into manageable groups.

5. **Whisper for Transcription:**
   - **Reasoning:** Whisper provides robust speech-to-text capabilities, which are necessary for accurately transcribing meeting videos.
   - **Choice:** Used Whisper for transcribing audio extracted from meeting videos.

## Dependencies

Ensure all dependencies are installed by running:

```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
openai
streamlit
chromadb
transformers
sentence-transformers
moviepy
whisper
PyPDF2
scikit-learn
numpy
```

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repository/meeting-management-system.git
   cd meeting-management-system
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys:**
   - **OpenAI GPT-4 API Key:** Set your API key in the `app.py` file.
   - **ChromaDB API Key:** Ensure ChromaDB client is correctly configured in `chromadb_utils.py`.

5. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

6. **Access the Application:**
   - Open a web browser and navigate to `http://localhost:8501` to interact with the application.

## Operating the System

### Uploading Documents

1. **Navigate to the Document Upload Section:**
   - Click on the “Upload relevant documents” section.
   - Upload text (`.txt`) or PDF (`.pdf`) files.

2. **Document Processing:**
   - Uploaded documents are processed to extract text and store embeddings.

### Managing Discussion Topics

1. **Submit Discussion Topics:**
   - Enter your name and discussion topics in the form.
   - Click “Submit Topics” to add them to the discussion list.

2. **Clustering and Agenda Generation:**
   - The system clusters discussion topics and generates a meeting agenda using GPT-4.

### Uploading and Transcribing Videos

1. **Navigate to the Video Upload Section:**
   - Click on “Upload a Meeting Video.”
   - Upload video files in supported formats (MP4, AVI, MKV).

2. **Transcription:**
   - The video is processed to extract audio, which is then transcribed into text using Whisper.

3. **Analysis of Discussion Topics:**
   - The transcription is compared to the list of discussion topics to identify covered and unresolved topics.

### Retrieving Relevant Information

1. **Retrieve Information:**
   - Click on the “Retrieve Relevant Information” button.
   - The system will display relevant information from uploaded documents based on discussion topics.

## Detailed Function Descriptions

### `gpt_summary.py`

- **`generate_gpt4_summary(context)`**
  - **Purpose:** Generates a summary or agenda from a given context using GPT-4.
  - **Parameters:** 
    - `context` – A string containing the information to be summarized.
  - **Returns:** Summary or agenda text.

- **`generate_detailed_summary(transcription, discussion_topics, decisions, action_items)`**
  - **Purpose:** Generates a detailed meeting summary based on transcription, discussion topics, decisions made, and action items.
  - **Parameters:**
    - `transcription` – Text from the video transcription.
    - `discussion_topics` – List of discussion topics.
    - `decisions` – Summary of decisions made.
    - `action_items` – List of action items.
  - **Returns:** Detailed summary text.

### `chromadb_utils.py`

- **`store_document_embeddings(documents)`**
  - **Purpose:** Stores document embeddings in a ChromaDB collection.
  - **Parameters:**
    - `documents` – List of document dictionaries with `"name"` and `"content"`.
  - **Behavior:** Creates or updates a ChromaDB collection with document embeddings.

- **`retrieve_relevant_information(query, documents)`**
  - **Purpose:** Retrieves relevant documents based on a query using semantic search.
  - **Parameters:**
    - `query` – The search query string.
    - `documents` – List of document dictionaries.
  - **Returns:** List of top 3 most similar documents' content.

### `document_utils.py`

- **`process_uploaded_files(uploaded_files)`**
  - **Purpose:** Extracts text from PDFs and decodes text files.
  - **Parameters:**
    - `uploaded_files` – List of uploaded files.
  - **Returns:** List of document dictionaries with `"name"` and `"content"`.

### `clustering.py`

- **`cluster_discussion_topics(discussion_data)`**
  - **Purpose:** Clusters discussion topics into groups using KMeans.
  - **Parameters:**
    - `discussion_data` – List of discussion topics.
  - **Returns:** Dictionary of clustered topics.

### `video_utils.py`

- **`transcribe_video(audio_path)`**
  - **Purpose:** Transcribes audio extracted from a video into text.
  - **Parameters:**
    - `audio_path` – Path to the audio file.
  - **Returns:** Transcribed text.

- **`analyze_discussion_topics(transcription, discussion_data)`**
  - **Purpose:** Analyzes transcription to determine which discussion topics are covered or unresolved.
  - **Parameters:**
    - `transcription` – Text from video transcription.
    - `discussion_data` – List of discussion topics.
  - **Returns:** Two lists: covered and unresolved topics.

## License

This project is licensed under the MIT Licensee
