# overworked-auto-reply

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/nmlyz/overworked-auto-reply/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/nmlyz/overworked-auto-reply/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

A tiny program that writes one out-of-office auto-reply line to a file:
the manager is a dashboard, it approved the leave, the pager did not,
and the pager has been muted.

Competition page: https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda

## Run it

```sh
python3 main.py
```

## What it does

Running `main.py` writes a single line to `/output/entry.txt`:

> My manager is a dashboard. It approved my leave. My pager did not. I have muted the pager.

Before writing anything, the program checks the line: it must be one
line, end with a full stop, stay under 159 characters, be exactly 90
characters long, and contain the words `dashboard`, `pager` and `leave`.
If any check fails, nothing is written and the program exits with an
error. After writing, it reads the file back and refuses to continue
unless what is on disk matches the validated line byte for byte.

## How it works

`main.py` is split into small functions: `build_line` returns the line,
`check_line` collects every problem with it, `write_entry` creates the
output directory if needed, writes the file and verifies it by reading
it back, and `main` ties them together. Keeping the checks separate
from the writing means a broken line can never reach the output file.

## Usage

```sh
python3 main.py
cat /output/entry.txt
```

The program uses only the Python standard library, so there is nothing
to install. The output file is written with mode `0644` and the result
is byte-identical on every run. To check that, run it twice and compare
the two outputs — they match exactly:

```sh
python3 main.py > /tmp/run1.txt
python3 main.py > /tmp/run2.txt
diff /tmp/run1.txt /tmp/run2.txt
```

## Files

- `main.py` — builds, validates and writes the out-of-office line.
- `LICENSE` — MIT license.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)</sub>
