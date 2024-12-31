import spacy
import requests

nlp = spacy.load("en_core_web_md")
api_key = "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"
url = "https://openrouter.ai/api/v1/chat/completions"

def get_response_from_llama(prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost:8000",  # Required by OpenRouter
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-2-13b-chat",  
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.8,
        "max_tokens": 150
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        try:
            generated_text = response.json()['choices'][0]['message']['content']
            return f"magic bubbles: {generated_text}"
        except KeyError:
            return "Error: Unexpected API response structure"
    else:
        return f"Error: {response.status_code}, {response.text}"

def chatbot(statement):
   response = get_response_from_llama(statement)
   return response



if __name__ == "__main__":
    print('Hello! I am bubbles! Ask me anything :D')
    while True:
        user = input('You: ')
        if user.lower() in ['q', 'exit']:
            print('Have a good day!')
            break
        response = chatbot(user)
        print(response)
