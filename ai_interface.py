import openai

openai.api_key = ''  # Replace with your OpenAI API key

def generate_response_with_context(query, context):
    """Generates a response using the OpenAI API, based on retrieved context."""
    prompt = f"Using the following context, answer the question:\n\nContext:\n{context}\n\nQuestion: {query}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

