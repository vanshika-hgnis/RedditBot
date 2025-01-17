import schedule
import time
from generate_content import generate_posts_with_mistral
from prompts import generate_post_prompt_with_top_posts
import praw
from dotenv import dotenv_values


def schedule_posts(posting_times, subreddit_name, keywords, num_posts=1):
    """
    Schedule Reddit posts at specified times with top posts and keywords integrated into the prompt.
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

    # Fetch top posts
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = []
    for post in subreddit.top(limit=5):  # Fetch top 5 posts
        top_posts.append({"title": post.title, "self_text": post.selftext})

    # Generate the post prompt with the top posts and keywords
    post_prompt = generate_post_prompt_with_top_posts(top_posts, keywords)

    # Specify the target subreddit for posting
    subreddit = reddit.subreddit(subreddit_name)

    def make_post():
        """Generate and submit a post."""
        try:
            # Generate post content using the Mistral model
            posts = generate_posts_with_mistral(post_prompt, num_posts)
            if posts:
                # Submit to Reddit
                post = subreddit.submit(
                    title=posts[0]["title"], selftext=posts[0]["self_text"]
                )
                post_url = post.url  # URL of the posted content
                print(f"Posted successfully at {time.strftime('%H:%M')}")
                return post.title, post.selftext, post_url
        except Exception as e:
            print(f"Error posting: {e}")
            return None, None, None

    # Schedule posts for each time
    posted_data = []
    for posting_time in posting_times:
        schedule.every().day.at(posting_time).do(make_post)
        print(f"Scheduled post for {posting_time}")

        # Store post data after it's made
        post_title, post_text, post_url = (
            make_post()
        )  # This triggers the post immediately for demo
        if post_title:
            posted_data.append((post_title, post_text, post_url))

    # Run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

    return posted_data  # Return list of posted data


if __name__ == "__main__":
    # Example usage
    times = ["18:17"]  # Posts at 6 PM
    subreddit_name = "testingground4bots"  # Example subreddit
    keywords = ["space", "physics", "quantum mechanics"]  # Example keywords
    schedule_posts(times, subreddit_name, keywords)
