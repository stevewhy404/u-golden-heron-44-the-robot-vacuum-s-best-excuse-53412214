"""The Robot Vacuum's Best Excuse — one line, max 140 characters."""

import os

LINE = "My cliff sensor called it a staircase, my bumper called it a wall, my map called it a no-go zone — so I left the dust there as evidence."

def main():
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
