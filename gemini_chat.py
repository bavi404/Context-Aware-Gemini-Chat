import google.generativeai as genai
import os
from dotenv import load_dotenv  

load_dotenv()  # Load environment variables from .env

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Please set your GEMINI_API_KEY environment variable.")

# Initialize Gemini client
genai.configure(api_key=GEMINI_API_KEY)


# Ask user to set temperature (default = 0.7 for a reason)
try:
    temp = float(input("Set creativity (temperature) [0.0 - 1.0, default 0.7]: ") or "0.7")
except ValueError:
    print("Invalid input. Using default temperature = 0.7")
    temp = 0.7

# Initialize chat model with memory
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

# ==== MULTIPLE TURNS ====

print("\nGemini Chat: Type your messages below. Type 'exit' to stop.\n")

# First input
user_input = input("You: ")
if user_input.strip().lower() == 'exit':
    exit()

response = chat.send_message(user_input, generation_config={"temperature": temp})
print("Gemini:", response.text)

# Second input
user_input = input("\nYou (follow-up): ")
if user_input.strip().lower() == 'exit':
    exit()

response = chat.send_message(user_input, generation_config={"temperature": temp})
print("Gemini:", response.text)

# Bonus: Third turn (optional)
user_input = input("\nYou (another follow-up): ")
if user_input.strip().lower() == 'exit':
    exit()

response = chat.send_message(user_input, generation_config={"temperature": temp})
print("Gemini:", response.text)
