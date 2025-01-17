# Reddit Mistral Bot

A Reddit bot that automatically generates and posts content using Mistral AI.

## Features

- Daily automated posting at user-specified times
- Content generation using Mistral AI
- Basic comment generation capability
- Error handling and logging
- Scheduled posting system

## Setup

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your credentials:

```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
MISTRAL_API_KEY=your_mistral_api_key
TARGET_SUBREDDIT=your_target_subreddit
```

4. Run the bot:

```bash
python src/bot.py
```

## Project Structure

- `src/`: Main source code
  - `bot.py`: Main bot implementation
  - `config.py`: Configuration management
  - `utils/`: Utility functions
    - `content_generator.py`: Mistral AI integration
    - `logger.py`: Logging configuration
- `logs/`: Log files
- `requirements.txt`: Project dependencies
- `.env`: Environment variables

## Configuration

- Adjust posting schedule in `bot.py`
- Modify content generation prompts in `utils/content_generator.py`
- Configure logging settings in `utils/logger.py`

## Error Handling

The bot includes comprehensive error handling and logging:

- All errors are logged to `logs/bot.log`
- Automatic retry mechanism for failed operations
- Detailed error messages for debugging

## License

MIT
