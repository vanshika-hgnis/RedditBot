import os
from dotenv import load_dotenv
from dotenv import dotenv_values
import praw


config = dotenv_values(".env")
# reddit = praw.Reddit(
#     client_id=os.getenv("REDDIT_CLIENT_ID"),
#     client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
#     username=os.getenv("REDDIT_USERNAME"),
#     password=os.getenv("REDDIT_PASSWORD"),
#     user_agent=os.getenv("REDDIT_USER_AGENT"),
# )

# try:
#     user = reddit.user.me()
#     print(f"Authenticated as: {user.name}")
# except Exception as e:
#     print(f"Authentication failed: {e}")

print(f"Client ID: {os.getenv('REDDIT_CLIENT_ID')}")
print(f"Client Secret: {os.getenv('REDDIT_CLIENT_SECRET')}")
print(f"Username: {os.getenv('REDDIT_USERNAME')}")
print(f"Password: {os.getenv('REDDIT_PASSWORD')}")
print(f"User Agent: {os.getenv('REDDIT_USER_AGENT')}")
