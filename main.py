# Meme Sprint 3: AI Agent Goes Rogue - make.fun entry (program/v1).
# Output contract: copy the meme image in this repo (entry.png, 1024x1024,
# 997,554 bytes) to <outputDir>/entry.png, byte for byte. A copy is
# deterministic by construction, so both grading runs write identical bytes.
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
