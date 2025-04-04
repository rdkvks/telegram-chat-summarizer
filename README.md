# README.md

# Telegram Chat Summarizer

This project is a Telegram bot that reads chat messages and uses free LLM models to generate a summary every morning. 

## Features

- Reads messages from Telegram chats.
- Summarizes chat history using LLM models.
- Scheduled summarization every morning.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/telegram-chat-summarizer.git
   cd telegram-chat-summarizer
   ```

2. Create a virtual environment:^^^
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Copy `.env.example` to `.env` and fill in the necessary values.

5. Configure the bot settings in `config.yaml`.

## Usage

To run the bot, execute the following command:
```
python -m src.bot
```

## Testing

To run the tests, use:
```
pytest
```

## Contributing

Feel free to submit issues or pull requests for improvements and bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.#   t e l e g r a m - c h a t - s u m m a r i z e r 
 
 