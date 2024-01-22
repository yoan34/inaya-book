import os
import time
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

from openai import OpenAI
from app.tools.enumerators import ModelType
from dotenv import load_dotenv

from app.tools.decorators import retry_api_call

load_dotenv()
api_key = os.environ.get("MISTRAL_API_KEY")
model = "mistral-tiny"

client = MistralClient(api_key=api_key)

class ChatGPT:
    def __init__(self, model: ModelType = ModelType.GPT_4):
        self.model = model
        self.mistral_api_key = os.environ.get("MISTRAL_API_KEY")
        self.mistral_client = MistralClient(api_key=self.mistral_api_key)
        self.openai_api_key = os.environ.get("OPENAI_API_KEY")
        self.openai_client = OpenAI(api_key=self.openai_api_key)

    #@retry_api_call(max_attempts=10, delay=2)
    def answer(self, question: str, context: str, temperature: float = 0.2):
        completion = self.openai_client.chat.completions.create(
            model=self.model.value,
            messages=[
                {'role': 'system', 'content': context},
                {"role": "user", "content": question},
            ],
            temperature=temperature,
        )
        answer = completion.choices[0].message.content
        tokens = completion.usage.total_tokens
        print(f"COMPLETION TOKEN: {completion.usage.completion_tokens}")
        return answer, tokens
    
    
    def answer_mistral(
        self,
        question: str,
        context: str,
        temperature: float = 0.7,
        max_retries: int = 3,
        retry_delay: int = 2
    ):
        messages = [
            ChatMessage(role="system", content=context),
            ChatMessage(role="user", content=question)
        ]
        for attempt in range(max_retries):
            try:
                chat_response = self.mistral_client.chat(
                    model="mistral-tiny",
                    messages=messages,
                )
                answer = chat_response.choices[0].message.content
                tokens = chat_response.usage.total_tokens
                return answer, tokens
            except Exception as e:
                print(f"Erreur lors de l'appel à Mistral: {e}")
                if attempt < max_retries - 1:
                    print(f"Réessai {attempt + 1}/{max_retries} dans {retry_delay} secondes...")
                    time.sleep(retry_delay)
                else:
                    raise
        chat_response = client.chat(
            model="mistral-tiny",
            messages=messages,
        )
        answer = chat_response.choices[0].message.content
        tokens = chat_response.usage.total_tokens
        return answer, tokens


if __name__ == "__main__":
    chat_gpt = ChatGPT()
    answer, tokens = chat_gpt.answer_mistral(question="Salut", context="You are a helpful assistant.")
    print(answer)
    print(f"token: {tokens}")