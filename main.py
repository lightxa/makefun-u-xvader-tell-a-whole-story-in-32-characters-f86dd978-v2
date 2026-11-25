"""Tell a Whole Story in 32 Characters -- variant 2.

Entry: "Dog Ate Homework, Then Router" (29 characters).

Why this name: the classic excuse "the dog ate my homework" is a setup
everyone knows, and the second beat reframes it as a real, worse event --
the dog actually did it, and then moved on to the router. One concrete
object (the router) carries the whole life of the story: a character (the
dog), a situation (homework time), and something that happened (the router
got eaten). The turn lands in the last word, and the reader fills in the
missing "ate the" themselves. A different story family from variant 1
(the roommate who moved out): this is a pet-escalation story, not a
domestic departure story.
"""

import os

ENTRY = "Dog Ate Homework, Then Router"


def check_entry(text: str) -> None:
    """Gate self-check mirroring the sealed scorer.

    The scorer requires /output/entry.txt to be UTF-8 text of 1 to 32
    characters, not only whitespace, on a single line.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 32):
        raise ValueError(f"entry must be 1 to 32 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main() -> None:
    check_entry(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
