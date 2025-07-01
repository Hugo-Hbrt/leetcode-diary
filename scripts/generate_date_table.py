import os
from collections import defaultdict

README_PATH = "README.md"
PROBLEMS_DIR = "problems"

def extract_date_and_title(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    title = next((line.split(": ")[1].strip() for line in lines if line.startswith("# Title")), None)
    date = next((line.split(": ")[1].strip() for line in lines if line.startswith("# Date")), None)
    return title, date

def insert_date_table(content, table):
    lines = content.split("\n")
    start_idx, end_idx = None, None

    # Find the existing "Problems solved by date" section
    for i, line in enumerate(lines):
        if line.startswith("## 📅 Problems solved by date"):
            start_idx = i
        elif start_idx is not None and line.startswith("## ") and not line.startswith("## 📅 Problems solved by date"):
            end_idx = i
            break

    # Remove the existing section if found
    if start_idx is not None:
        if end_idx is None:
            lines = lines[:start_idx]
        else:
            lines = lines[:start_idx] + lines[end_idx:]

    # Insert the new table before the "Roadmap" section
    for i, line in enumerate(lines):
        if line.startswith("## 🧭 Roadmap"):
            return "\n".join(lines[:i]).strip() + "\n\n" + table.strip() + "\n\n" + "\n".join(lines[i:]).strip()
    return content.strip()

def generate_date_table():
    date_to_problems = defaultdict(list)
    for root, dirs, files in os.walk(PROBLEMS_DIR):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                title, date = extract_date_and_title(file_path)
                if title and date:
                    date_to_problems[date].append(title)
    
    table_content = "\n## 📅 Problems solved by date\n\n| Date | Problems |\n|------|----------|\n"
    for date, problems in sorted(date_to_problems.items()):
        problems = ["- " + problem for problem in problems]
        table_content += f"| {date} | {'<br>'.join(problems)} |\n"
    
    with open(README_PATH, "r") as f:
        readme_content = f.read()
    
    updated_content = insert_date_table(readme_content, table_content)
    
    with open(README_PATH, "w") as f:
        f.write(updated_content)

if __name__ == "__main__":
    generate_date_table()
