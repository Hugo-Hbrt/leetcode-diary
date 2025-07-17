import json
import datetime
from sync_training_data import update_training_data

def load_training_data(path):
    """Load the training data JSON file."""
    with open(path, 'r') as file:
        return json.load(file)

def save_training_data(path, data):
    """Save the training data to the JSON file."""
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

def get_due_problems(data):
    """Get problems that are due for review today."""
    today = datetime.date.today()
    due_problems = []
    for unique_id, problem in data.items():
        next_review = problem.get("next_review")
        if next_review:
            next_review_date = datetime.datetime.strptime(next_review, "%Y-%m-%d").date()
            if next_review_date <= today:
                due_problems.append((unique_id, problem))
    return due_problems

def update_problem(problem, success):
    """Update the problem's review data based on success or failure."""
    today = datetime.date.today()
    if success:
        problem["interval"] *= 2  # Double the interval
        problem["success_streak"] += 1
    else:
        problem["interval"] = 1  # Reset interval to 1 day
        problem["success_streak"] = 0
    problem["last_reviewed"] = today.strftime("%Y-%m-%d")
    next_review_date = today + datetime.timedelta(days=problem["interval"])
    problem["next_review"] = next_review_date.strftime("%Y-%m-%d")

def spaced_repetition_session(data):
    """Run a spaced repetition training session."""
    due_problems = get_due_problems(data)
    if not due_problems:
        print("No problems are due for review today.")
        return

    print(f"{len(due_problems)} problems are due for review today:")
    for unique_id, problem in due_problems:
        print(f"- {problem['title']}")

    for unique_id, problem in due_problems:
        print(f"\nReviewing: {problem['title']}")
        while True:
            user_input = input("Was the training successful? (y/n/q to quit): ").strip().lower()
            if user_input == 'y':
                update_problem(problem, success=True)
                break
            elif user_input == 'n':
                update_problem(problem, success=False)
                break
            elif user_input == 'q':
                print("Exiting training session. Progress will be saved.")
                return
            else:
                print("Invalid input. Please enter 'y', 'n', or 'q'.")

def main():
    json_path = 'training/training_data.json'

    # Update training data from README.md
    update_training_data()
    
    training_data = load_training_data(json_path)
    spaced_repetition_session(training_data)
    save_training_data(json_path, training_data)

if __name__ == "__main__":
    main()
