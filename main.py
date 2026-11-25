"""One Line, One Laugh - a single funny line, whole on its own.

The program writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output), with no trailing newline. The bounty's gate: entry.txt must be
UTF-8 text of 1 to 140 characters, not only white space.
"""

import os

TEXT = "I told my AI assistant I felt lonely, so it booked a meeting with itself — and marked me optional."
# Why this line: the setup is a small human confession (lonely), the turn is
# the assistant solving it the way a calendar-obsessed coworker would, and
# the punchline flips the power dynamic - the human is the optional one.
# The line is 98 characters: short enough to read in a breath, long enough
# for the setup, the turn and the sting to each land.


def gate(text):
    """Check the 1-140 character gate: UTF-8, 1-140 chars, not only
    whitespace, no leading or trailing whitespace, a single line."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry is %d chars, gate is 1-140" % len(text))
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    gate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        raw = f.read()
    read_back = raw.decode("utf-8")
    if read_back != TEXT:
        raise ValueError("read-back differs from TEXT")
    gate(read_back)
    print("wrote %d chars to %s" % (len(TEXT), path))


if __name__ == "__main__":
    main()
