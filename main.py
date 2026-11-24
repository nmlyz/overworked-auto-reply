#!/usr/bin/env python3
"""Write one out-of-office auto-reply to /output/entry.txt.

The reply is one line: a manager that is a dashboard approved the
leave, the pager did not, and the pager has been muted. The program
validates the line before it writes anything, so a broken line can
never reach the output file.
"""

import os
import sys

# The reply, exactly as it is meant to be read.
LINE = (
    "My manager is a dashboard. "
    "It approved my leave. "
    "My pager did not. "
    "I have muted the pager."
)

# Where the entry goes. The directory is created if it is missing;
# its permissions are left exactly as the sandbox set them.
OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"

# Guards that keep the output honest: the line must be a single line,
# end with a full stop, and stay within the competition's 159-character
# cap. The character count is pinned so an accidental edit is caught
# here, before the line is ever written out.
MAX_LENGTH = 159
EXPECTED_LENGTH = 90
REQUIRED_WORDS = ("dashboard", "pager", "leave")


def build_line() -> str:
    """Return the reply line, stripped of any stray whitespace."""
    line = LINE.strip()
    return line


def check_line(line: str) -> list[str]:
    """Collect every problem with a candidate line; empty means fine."""
    problems = []
    if not line:
        problems.append("line is empty")
    if not line.strip():
        problems.append("line is only white space")
    if "\n" in line or "\r" in line:
        problems.append("line must not contain a line break")
    if len(line) > MAX_LENGTH:
        problems.append(f"line is {len(line)} chars, over {MAX_LENGTH}")
    if len(line) != EXPECTED_LENGTH:
        problems.append(
            f"line is {len(line)} chars, expected {EXPECTED_LENGTH}"
        )
    if not line.endswith("."):
        problems.append("line must end with a full stop")
    for word in REQUIRED_WORDS:
        if word not in line:
            problems.append(f"line is missing the word {word!r}")
    return problems


def output_path() -> str:
    """Join the output directory and file name."""
    return os.path.join(OUTPUT_DIR, OUTPUT_NAME)


def write_entry(line: str) -> str:
    """Write the line to /output/entry.txt and return the path.

    The file is read back after writing: what is on disk must be
    byte for byte the validated line, with nothing added.
    """
    path = output_path()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line:
        raise ValueError("written entry does not match the validated line")
    return path


def main() -> int:
    """Validate the line, write it out, and print it."""
    line = build_line()
    problems = check_line(line)
    if problems:
        for problem in problems:
            print(f"invalid reply: {problem}", file=sys.stderr)
        return 1
    path = write_entry(line)
    print(line)
    print(f"wrote {len(line)} characters to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
