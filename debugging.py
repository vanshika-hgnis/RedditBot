from dotenv import dotenv_values
import praw


config = dotenv_values(".env")
print("Loaded .env values:")
print(config)

# import os
# from dotenv import load_dotenv, dotenv_values

# print("Loaded .env values:")
# print(dotenv_values(".env"))

# print("\nLoaded Environment Variables:")
# for key, value in os.environ.items():
#     if "REDDIT" in key:
#         print(f"{key}: {value}")

from dotenv import dotenv_values

config = dotenv_values(".env")

reddit = praw.Reddit(
    client_id=config["REDDIT_CLIENT_ID"],
    client_secret=config["REDDIT_CLIENT_SECRET"],
    username=config["REDDIT_USERNAME"],
    password=config["REDDIT_PASSWORD"],
    user_agent=config["REDDIT_USER_AGENT"],
)

try:
    user = reddit.user.me()
    print(f"Authenticated as: {user.name}")
except Exception as e:
    print(f"Authentication failed: {e}")
