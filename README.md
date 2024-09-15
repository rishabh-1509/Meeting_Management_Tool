# Meeting Management Tool

## Overview

This tool is designed to manage and document meetings efficiently. It leverages various AI and machine learning technologies to handle meeting transcripts, discussion topics, and documents. The system includes features for summarizing meetings, generating agendas, analyzing covered and unresolved topics, and retrieving relevant information from uploaded documents.

## Architecture and Flow

1. **Document Upload and Processing:**
   - **Text Files:** Extract content directly.
   - **PDF Files:** Use `PyPDF2` to extract text from each page.
   - Documents are processed and stored with their embeddings in ChromaDB for retrieval.

2. **Discussion Topics Clustering:**
   - Discussion topics are collected and clustered using KMeans to group similar topics.
   - Clusters are used to generate structured meeting agendas.

3. **Video Processing:**
   - Videos are uploaded, and audio is extracted using `moviepy`.
   - Whisper is used for transcription of the audio.
   - Transcription is analyzed to identify covered and unresolved discussion topics.

4. **GPT-4 Integration:**
   - **Summaries and Agendas:** GPT-4 generates concise summaries, detailed meeting summaries, and agendas based on provided context.
   - **Document Retrieval:** Relevant documents are retrieved based on discussion topics using semantic search and cosine similarity.

## Dependencies

To run this tool, you need the following dependencies. You can install them using `pip`:

```bash
pip install openai streamlit chromadb transformers sentence-transformers moviepy whisper PyPDF2 scikit-learn
```

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/meeting-management-tool.git
   cd meeting-management-tool
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys:**
   - Ensure you have valid API keys for OpenAI GPT and other services. Set these keys in the `app.py` and `gpt_summary.py` files.

4. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

## Usage Guidelines

1. **Upload Documents:**
   - Upload text or PDF files to be processed and stored for retrieval.

2. **Submit Discussion Topics:**
   - Enter discussion topics in the provided form. Topics are clustered, and an agenda is generated.

3. **Upload Video:**
   - Upload meeting videos to transcribe and analyze discussion topics.

4. **Retrieve Relevant Information:**
   - Use the "Retrieve Relevant Information" button to get relevant documents based on discussion topics.

## File Descriptions

- `app.py`: Main application script that integrates all components, including file upload, discussion topic management, video processing, and interaction with GPT-4.
- `gpt_summary.py`: Contains functions for generating summaries, agendas, and detailed meeting summaries using GPT-4.
- `document_utils.py`: Includes functions for processing text and PDF documents.
- `video_utils.py`: Handles video transcription and analysis.
- `clustering.py`: Manages clustering of discussion topics using KMeans.

## Design and Implementation Choices

- **Prompt Design for GPT-4:** Prompts are carefully crafted to ensure GPT-4 generates precise and relevant outputs.
- **Document and Video Processing:** The system uses open-source libraries to handle different file formats and AI models for transcription and clustering.
- **Modular Code:** Code is divided into modules for better maintainability and organization.

## Assumptions

- The API keys for OpenAI GPT and ChromaDB are valid and properly configured.
- Uploaded documents are in supported formats (TXT, PDF) and videos are in supported formats (MP4, AVI, MKV).

## Troubleshooting

- **Common Errors:**
  - If you encounter issues with document processing or video transcription, ensure the file formats are correct and not corrupted.
  - Check API keys and internet connectivity if the application fails to interact with external services.

For further questions or issues, please refer to the documentation of the respective libraries used or contact support.
