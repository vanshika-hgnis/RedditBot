from dotenv import dotenv_values
import praw

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


# subreddit = reddit.subreddit(config["TARGET_SUBREDDIT"])
# print(subreddit)
# top_25 = subreddit.hot(limit=25, timelimit="all")
# print(top_25)
# for sub in top_25:
#     print(sub.title)

# subreddit = reddit.subreddit("testingground4bots")
# subreddit.submit("Test Post", selftext="This is a test post from a bot.")
# Specify the subreddit
subreddit_name = "askscience"
subreddit = reddit.subreddit(subreddit_name)

# Extract top posts
print(f"Subreddit: {subreddit.display_name}")
print(f"Description: {subreddit.public_description}")
print("\nTop Posts:\n")

for post in subreddit.top(limit=2):  # Fetch top 5 posts
    print(f"Title: {post.title}")
    print(f"Self-text: {post.selftext[:100]}...")  # Print the first 100 characters
    print(f"Score: {post.score}")
    print("Comments:")
    post.comments.replace_more(limit=0)  # Flatten comment tree
    for comment in post.comments.list()[:5]:  # Fetch top 5 comments
        print(f"  - {comment.body[:100]}...")  # Print the first 100 characters
    print("-" * 40)

# Fetch guidelines
print("\nSubreddit Guidelines (Rules):\n")
for rule in subreddit.rules:
    print(f"- {rule.short_name}: {rule.description}")
