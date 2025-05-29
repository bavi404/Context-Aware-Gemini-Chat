# Gemini Multi-Turn Chat

A simple context-aware chatbot using Google Gemini's Free API (gemini-1.5-flash). It supports multi-turn conversations and preserves context across turns.


##  What it does

- Prompts the user for input via the console
- Sends user input to Gemini and gets a response
- Keeps track of chat history for contextual replies
- Allows configuring temperature (response creativity)


##  How to Run

### 1. Clone this repository

git clone https://github.com/bavi404/gemini-multi-turn-chat
cd gemini-multi-turn-chat

### 2. Set your Gemini API key

export GEMINI_API_KEY="your-google-api-key"

### 3. Install dependencies

pip install google-generativeai

### 4. Run the script

python gemini_chat.py

## Example Features

* Multi-turn context-aware dialogue
* Adjustable `temperature` for creativity
* Simple command-line interaction

##  License

MIT License
