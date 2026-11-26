import os

ENTRY = "The One-Robot Band \u2014 hit single \u201cI Open for Myself (and Carry My Own Amps).\u201d\n"

# The gate requires 1-200 characters of UTF-8 text; fail loudly if we drift.
assert 1 <= len(ENTRY) <= 200, len(ENTRY)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
