# Bav Bot

Bav Bot is a simple interactive chatbot built using Streamlit and OpenAI's GPT-3.5-turbo. The bot allows users to have a conversation with an AI assistant, with the conversation context preserved across interactions.

## Features

- **Interactive Chat Interface**: Users can type in prompts and receive responses from the AI in a chat-like format.
- **Session Persistence**: The conversation context is maintained using Streamlit's session state, allowing for a coherent and continuous conversation.
- **Streaming Responses**: The responses from the AI are streamed to give a more dynamic and real-time interaction experience.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/bav-bot.git
    cd bav-bot
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set your OpenAI API key:

    Open the script `bav_bot.py` and replace the placeholder API key with your actual OpenAI API key:

    ```python
    openai.api_key = "your-openai-api-key"
    ```

## Usage

To run the chatbot, use the following command:

```sh
streamlit run bav_bot.py
