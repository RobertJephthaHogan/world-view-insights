from openai import OpenAI
from app.config import Settings


client = OpenAI(api_key=Settings().WVI_OPENAI_API_KEY)


class OpenAiService:
    
    async def test_open_ai():
        
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
        )
        print(completion.choices[0].message)    
    
    