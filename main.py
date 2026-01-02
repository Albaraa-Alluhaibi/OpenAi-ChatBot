import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

BOT_NAME = "Alicia"

def chat_loop():
    # Memory exists ONLY while program is running
    messages = [
        {"role": "system", "content": "You are Alicia, an AI assistant."}
    ]

    print(f"{BOT_NAME}: Hi! I am your AI assistant Alicia.")
    print("Type 'exit , quit , bye' to end the chat.\n")

    while True:
        user_input = input("User: ").strip()

        if user_input.lower() in ["exit", "bye", "quit"]:
            print(f"{BOT_NAME}: Goodbye!")
            break

        if not user_input:
            continue

        # Add user message to memory
        messages.append({"role": "user", "content": user_input})

        # Send conversation so far
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=messages
        )

        reply = response.output_text.strip()

        # Add assistant reply to memory
        messages.append({"role": "assistant", "content": reply})

        print(f"{BOT_NAME}: {reply}\n")

if __name__ == "__main__":
    chat_loop()
