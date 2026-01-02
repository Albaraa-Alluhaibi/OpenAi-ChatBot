import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("Chatbot started. Type 'exit' to quit.\n")

while True:
    user_text = input("You: ").strip()
    if user_text.lower() in ("exit", "quit"):
        break

    messages.append({"role": "user", "content": user_text})

    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
    )

    reply = resp.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print(f"\nBot: {reply}\n")
