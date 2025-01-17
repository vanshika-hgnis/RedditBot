# Reddit Mistral Bot

About
A Reddit bot that automatically generates and posts content using Mistral AI.The user can also schedules post by time slots.

## Features

- Daily automated posting at user-specified times
- Content generation using Mistral AI
- Basic comment generation capability
- Error handling and logging
- Scheduled posting system

## Streamlit App

## Base Implemenation

![alt text](db/image.png)
![alt text](db/image1.png)

## Methodology

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
streamlit run app.py
```

## License

MIT
