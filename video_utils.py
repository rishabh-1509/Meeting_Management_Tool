import whisper
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def transcribe_video(audio_path):
    model_whisper = whisper.load_model('base')
    transcription = model_whisper.transcribe(audio_path)['text']
    return transcription

def analyze_discussion_topics(transcription, discussion_data):
    covered_topics = []
    unresolved_topics = []
    
    for topic in discussion_data:
        topic_embedding = model.encode(topic)
        transcription_embedding = model.encode(transcription)
        similarity = cosine_similarity([topic_embedding], [transcription_embedding])[0][0]
        if similarity > 0.7:
            covered_topics.append(topic)
        else:
            unresolved_topics.append(topic)
    
    return covered_topics, unresolved_topics
