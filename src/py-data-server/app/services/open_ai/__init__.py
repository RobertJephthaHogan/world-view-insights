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
    
    
    async def write_competitor_article(competitor_article):
        
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a high level financial journalist, skilled in explaining financial topics happening in the news better than anyone else."},
            {"role": "user", "content": f"I am your boss. Our competitor wrote a news article before us and we are covering the exact same topic \
                    Write a better article than this {competitor_article}   \
                "}
        ]
        )
        print(completion.choices[0].message)    
        return completion
    