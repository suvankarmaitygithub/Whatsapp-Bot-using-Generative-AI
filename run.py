import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def text_resources(prompt: str) -> dict:
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f'Human: {prompt} \nAI:',
            max_tokens=150,
            temperature=0.9,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["Human:","AI:"]
        )
        return {
            'status':1,
            'response':response['choices'][0]['text']
        }
    except:
        return {
            'status':0,
            'response':''
        }