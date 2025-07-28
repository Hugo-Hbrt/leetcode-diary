import os
import json
import datetime
from utils import slugify

def is_valid_markdown_table(line):
    """Check if a line is a valid Markdown table row."""
    return line.startswith('|') and '|' in line and not line.startswith('|---')  # Exclude header separator

def parse_readme(path):
    """Parse the Markdown table in README.md and return a list of problems."""
    problems = []
    with open(path, 'r') as file:
        lines = file.readlines()
        in_table = False
        for line in lines:
            if '| Date | Problems |' in line:  # Detect table header
                in_table = True
                continue
            if in_table and line.strip() == '':
                break  # End of table
            if in_table and line.startswith('|') and is_valid_markdown_table(line):
                columns = [col.strip() for col in line.split('|')[1:-1]]
                date, problems_list = columns
                for problem in problems_list.split('<br>'):
                    problem_title = problem.strip()[2:]
                    problems.append({
                        "title": problem_title,
                        "date": date
                    })
    return problems

def load_or_create_training_data(path):
    """Load the training data JSON file or create it if it doesn't exist."""
    if os.path.exists(path):
        with open(path, 'r') as file:
            return json.load(file)
    return {}

def get_nth_next_day(date_str, n):
    """Get the nth next day from a given date string."""
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    nth_next_day = date + datetime.timedelta(days=n)
    return nth_next_day.strftime("%Y-%m-%d")

def sync_training_data(problems, data):
    """Synchronize the problems from README.md with the training data."""
    newly_added = []
    for problem in problems:
        unique_id = slugify(problem["title"])
        if unique_id not in data:
            # Compute next review date as problem solved date + 1 day
            solved_date = problem["date"]
            next_review_date = get_nth_next_day(solved_date, 1)

            data[unique_id] = {
                "title": problem["title"],
                "last_reviewed": problem["date"],
                "next_review": next_review_date,
                "interval": 1,
                "success_streak": 0
            }
            newly_added.append(problem["title"])
    return newly_added

def save_training_data(path, data):
    """Save the training data to the JSON file."""
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

def update_training_data():
    readme_path = 'README.md'
    json_path = 'training/training_data.json'

    problems = parse_readme(readme_path)
    training_data = load_or_create_training_data(json_path)
    newly_added = sync_training_data(problems, training_data)
    save_training_data(json_path, training_data)

    if newly_added:
        print("Newly added problems:")
        for problem in newly_added:
            print(f"- {problem}")
    else:
        print("No new problems added.")
