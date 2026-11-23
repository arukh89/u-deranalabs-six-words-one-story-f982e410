"""Six Words, One Story: write one complete six-word story to /output/entry.txt.

The story is written exactly, with no trailing newline: six words, 36
characters, inside the gate's 1-60 character window.
"""

import os

STORY = "The letter arrived fifty years late."


def main():
    words = STORY.split()
    assert len(words) == 6, "story must be exactly six words"
    assert 1 <= len(STORY) <= 60 and STORY.strip(), "story must be 1-60 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
