# prompts.py


def generate_post_prompt_with_top_posts(top_posts, keywords):
    """
    Generate a post prompt using the top 5 posts and user-specified keywords.

    Args:
        top_posts (list): A list of top 5 posts (dictionaries with 'title' and 'self_text').
        keywords (list): List of keywords provided by the user.

    Returns:
        str: The generated prompt string.
    """
    # Extract titles and self-texts from the top posts
    top_posts_text = "\n".join(
        [
            f"Title: {post['title']}\nSelf-text: {post['self_text'][:200]}..."
            for post in top_posts
        ]
    )

    # Convert keywords into a string
    keywords_text = ", ".join(keywords)

    # Format the final post prompt
    post_prompt = f"""
    You are a knowledgeable and curious Reddit user creating posts for the subreddit r/askscience. Posts should spark scientific curiosity or provide interesting insights in a conversational, natural, and human-like tone.

    Here are the top 5 posts from the subreddit to give you an idea of the style:
    {top_posts_text}

    Keywords: {keywords_text}

    Based on this information, generate a post with the following format:
    {{
        "title": "Your attention-grabbing title here",
        "self_text": "The additional details or context here. End with a thought-provoking question to invite discussion."
    }}

    Ensure the post is relevant to the subreddit, follows its rules, and provides accurate information. Now generate a post.
    """

    return post_prompt
