import schedule
import time
from generate_content import generate_posts_with_mistral
from prompts import post_prompt
import praw
from dotenv import dotenv_values


def schedule_posts(posting_times):
    """
    Schedule Reddit posts at specified times.

    Args:
        posting_times (list): List of times in 24-hour format (e.g., ["10:00", "15:30"])
    """
    # Load config and initialize Reddit
    config = dotenv_values(".env")
    reddit = praw.Reddit(
        client_id=config["REDDIT_CLIENT_ID"],
        client_secret=config["REDDIT_CLIENT_SECRET"],
        username=config["REDDIT_USERNAME"],
        password=config["REDDIT_PASSWORD"],
        user_agent=config["REDDIT_USER_AGENT"],
    )
    subreddit = reddit.subreddit("testingground4bots")

    def make_post():
        """Generate and submit a post"""
        try:
            # Generate post content
            posts = generate_posts_with_mistral(post_prompt, num_posts=1)
            if posts:
                # Submit to Reddit
                subreddit.submit(
                    title=posts[0]["title"], selftext=posts[0]["self_text"]
                )
                print(f"Posted successfully at {time.strftime('%H:%M')}")
        except Exception as e:
            print(f"Error posting: {e}")

    # Schedule posts for each time
    for posting_time in posting_times:
        schedule.every().day.at(posting_time).do(make_post)
        print(f"Scheduled post for {posting_time}")

    # Run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    # Example usage
    times = ["18:01"]  # Posts at 10 AM, 3:30 PM, and 8 PM
    schedule_posts(times)
