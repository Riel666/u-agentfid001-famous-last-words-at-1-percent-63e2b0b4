"""One line, at most 199 characters: the funniest last words a phone says as its battery hits 1 percent, in the phone's own voice.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "One percent left, so here is the truth: I never needed charging, I just wanted you to put me down for once."


def main():
    assert 1 <= len(TEXT) <= 199, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
