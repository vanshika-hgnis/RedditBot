import streamlit as st
from reddit_posts_sheduler import schedule_posts


def main():
    st.title("Reddit Post Scheduler")

    # Collect user inputs
    subreddit_name = st.text_input("Enter Subreddit Name", "testingground4bots")

    # Input for keywords
    keywords_input = st.text_input("Enter Keywords (comma-separated)", "")
    keywords = (
        [keyword.strip() for keyword in keywords_input.split(",")]
        if keywords_input
        else []
    )

    # Input for number of posts
    num_posts = st.number_input(
        "Enter Number of Posts to Schedule", min_value=1, max_value=5, value=1
    )

    # Dynamically generate time input fields based on number of posts
    posting_times = []
    for i in range(num_posts):
        time_slot = st.text_input(
            f"Enter Posting Time Slot {i+1} (24-hour format, e.g., 18:00)", ""
        )
        posting_times.append(time_slot)

    # Initialize a variable to store the result of the posts
    posted_data = None

    if st.button("Schedule Posts"):
        # Check if times are provided
        if all(posting_times) and keywords:
            # Schedule the posts and get the posted data
            posted_data = schedule_posts(
                posting_times, subreddit_name, keywords, num_posts
            )

            # If posts were made, display them
            if posted_data:
                st.success("Posts have been scheduled successfully!")

                for post_title, post_text, post_url in posted_data:
                    # Display the post title
                    st.subheader(post_title)

                    # Display the post content
                    st.write(post_text)

                    # Display the URL of the post
                    st.markdown(f"[View Post on Reddit]({post_url})")

        else:
            st.error("Please provide valid inputs for keywords and posting times.")


if __name__ == "__main__":
    main()
