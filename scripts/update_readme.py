import os
import re

README_PATH = "README.md"
PROBLEMS_DIR = "problems"

def count_problems():
    total = 0
    for root, dirs, files in os.walk(PROBLEMS_DIR):
        for file in files:
            if file.endswith(".py") or file.endswith(".md") or file.endswith(".cpp"):
                total += 1
    return total

def update_readme(count):
    with open(README_PATH, "r") as f:
        content = f.read()

    updated = re.sub(r"- Total Problems Solved: \*\*\d+\*\*", 
                     f"- Total Problems Solved: **{count}**", 
                     content)

    with open(README_PATH, "w") as f:
        f.write(updated)

if __name__ == "__main__":
    solved_count = count_problems()
    print(f"Total problems solved: {solved_count}")
    update_readme(solved_count)
