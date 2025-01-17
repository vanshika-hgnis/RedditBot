import json
import re
from dotenv import dotenv_values
from mistralai import Mistral


def generate_posts_with_mistral(prompt, num_posts=1):
    """
    Generate AI-generated posts using Mistral and extract titles and self-texts from JSON.

    Args:
        prompt (str): The prompt to generate content.
        num_posts (int): The number of posts to generate.

    Returns:
        list: A list of dictionaries with 'title' and 'self_text' for each post.
    """
    # Load API key from environment variables
    config = dotenv_values(".env")
    api_key = config.get("MISTRAL_API_KEY")

    if not api_key:
        raise ValueError("MISTRAL_API_KEY not found in .env file.")

    # Set up Mistral client and model
    model = "mistral-small-latest"
    client = Mistral(api_key=api_key)

    # Generate posts
    posts = []
    for _ in range(num_posts):
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": prompt,
                },
            ],
        )
        response_content = chat_response.choices[0].message.content
        print("Raw Response:", response_content)

        # Attempt to clean and parse JSON response
        try:
            # Remove any leading/trailing spaces and fix potential issues
            cleaned_content = re.sub(r"[\r\n]+", "", response_content.strip())

            # Look for JSON-like structure
            json_start = cleaned_content.find("{")
            json_end = cleaned_content.rfind("}")

            if json_start != -1 and json_end != -1:
                # Extract valid JSON substring
                json_data = cleaned_content[json_start : json_end + 1]
                post = json.loads(json_data)

                # Ensure required fields exist
                if "title" in post and "self_text" in post:
                    posts.append(
                        {"title": post["title"], "self_text": post["self_text"]}
                    )
                else:
                    raise ValueError("JSON is missing required fields.")
            else:
                raise ValueError("No valid JSON found in response.")

        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error parsing JSON: {e}")
            posts.append(
                {"title": "Error Parsing Title", "self_text": "Error Parsing Self-text"}
            )

    return posts


# # Example usage
# if __name__ == "__main__":
#     from prompts import post_prompt  # Assuming 'post_prompt' is defined in prompts.py

#     # Prompt and number of posts
#     prompt = post_prompt
#     num_posts = 1  # Adjust as needed

#     # Generate posts
#     try:
#         posts = generate_posts_with_mistral(prompt, num_posts)
#         for idx, post in enumerate(posts, 1):
#             print(
#                 f"Post {idx}:\nTitle: {post['title']}\nSelf-text: {post['self_text']}\n"
#             )
#     except Exception as e:
#         print(f"Error: {e}")
