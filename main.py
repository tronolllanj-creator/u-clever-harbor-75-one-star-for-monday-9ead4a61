import os


LINE = "The 'Monday Special' arrived as gray leftover Sunday, the manager was unapologetic, and the check demanded payment for all hours after."


def main():
    content = LINE + "\n"
    if not (1 <= len(content) <= 180 and content.strip() and len(content.split()) <= 25 and content.count('\n') == 1):
        raise ValueError("entry failed validation")
    out = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out, "entry.txt")
    os.makedirs(out, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    if os.path.abspath(out) != os.path.abspath("/output"):
        try:
            os.makedirs("/output", exist_ok=True)
            with open(os.path.join("/output", "entry.txt"), "w", encoding="utf-8") as f2:
                f2.write(content)
        except Exception:
            pass
    print(path, len(content))  # one line, 1-180 chars, at most 25 words


if __name__ == "__main__":
    main()
