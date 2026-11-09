import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("Environment variable OPENROUTER_API_KEY not set")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
def main():
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
            }
        ],
    )

    if response.usage is None:
        raise RuntimeError("API request failed")
    print(f"Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}")
    print(f"Response:\n{response.choices[0].message.content}")


if __name__ == "__main__":
    main()
