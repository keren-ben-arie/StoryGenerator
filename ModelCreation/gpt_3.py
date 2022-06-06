import openai
from StoryTeller.logic import image_to_text

API_KEY = "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"

def generate_story(words):
    openai.api_key = API_KEY
    prompt = f"Generate a philosophical story that includes the words: {words}"
    response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=100)
    story = response["choices"][0]["text"]
    return story
