from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

# Conversation history starts with the system prompt
messages = [
    {
        "role": "system",
        "content": "You are the sale person. Be polite and humble with the customers",
    }
]

print("Hey! I am chatty. How can i assist you!")

while True:
    user_input = input("You: ").strip()

    # Skip empty input
    if not user_input:
        continue

    # Exit condition
    if user_input.lower() in ("exit", "quit"):
        print("Chatty: Thank you for visiting. Have a great day!")
        break

    # Add the user's message to history
    messages.append({"role": "user", "content": user_input})

    response = client.responses.create(
        input=messages,
        model="openai/gpt-oss-20b",
    )

    reply = response.output_text
    print(f"Chatty: {reply}\n")

    # Add the bot's reply to history so it remembers the conversation
    messages.append({"role": "assistant", "content": reply})