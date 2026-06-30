import os
from datetime import datetime


def save_story(prompt, genre, stories):
    """
    Save generated stories to a text file.
    """

    # Create stories folder if it doesn't exist
    os.makedirs("stories", exist_ok=True)

    # Create unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"story_{timestamp}.txt"

    filepath = os.path.join("stories", filename)

    # Write story to file
    with open(filepath, "w", encoding="utf-8") as file:

        file.write("=" * 50 + "\n")
        file.write("AI Dungeon Story Generator\n")
        file.write("=" * 50 + "\n\n")

        file.write(f"Genre:\n{genre}\n\n")

        file.write("Prompt:\n")
        file.write(prompt + "\n\n")

        file.write("-" * 50 + "\n\n")

        for index, story in enumerate(stories, start=1):

            file.write(f"Story {index}\n\n")

            file.write(story)

            file.write("\n\n")

            file.write("-" * 50 + "\n\n")

        file.write("=" * 50 + "\n")

        file.write(
            f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

    return filepath