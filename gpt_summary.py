import openai

openai.api_key = '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'

def generate_gpt4_summary(context):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=context,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def generate_detailed_summary(transcription, discussion_topics, decisions, action_items):
    context = f"Transcription: {transcription}\nDiscussion Topics: {discussion_topics}\nDecisions: {decisions}\nAction Items: {action_items}\nGenerate a meeting summary."
    return generate_gpt4_summary(context)
