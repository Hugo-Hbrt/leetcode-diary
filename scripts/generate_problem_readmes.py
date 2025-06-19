import os

PROBLEMS_DIR = "problems"

def generate_readme_for_subfolder(subfolder_path):
    readme_content = "# Problems solved\n\n"
    table_rows = []
    problem_sections = []

    for file_name in os.listdir(subfolder_path):
        if file_name.endswith(".py"):
            problem_path = os.path.join(subfolder_path, file_name)
            with open(problem_path, "r") as f:
                code_lines = f.readlines()
            
            # Extract problem metadata from the header
            title = next((line.split(": ")[1].strip() for line in code_lines if line.startswith("# Title")), "Unknown Title")
            link = next((line.split(": ")[1].strip() for line in code_lines if line.startswith("# Link")), "Unknown Link")
            difficulty = next((line.split(": ")[1].strip() for line in code_lines if line.startswith("# Difficulty")), "Unknown Difficulty")
            
            # Filter out header comments
            code = "".join(line for line in code_lines if not line.strip().startswith("#"))
            
            # Add to table
            table_rows.append(f"| {title} | [{link}]({link}) | {difficulty} |")
            
            # Add problem section
            problem_sections.append(f"## {title}\n\n```py\n{code}\n```\n")

    # Generate table
    if table_rows:
        readme_content += "| Problem | Link | Difficulty |\n"
        readme_content += "|---------|------|------------|\n"
        readme_content += "\n".join(table_rows) + "\n\n"

    # Add problem sections
    readme_content += "\n".join(problem_sections)

    # Write README.md to subfolder
    readme_path = os.path.join(subfolder_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(readme_content)

def generate_readmes():
    for subfolder in os.listdir(PROBLEMS_DIR):
        subfolder_path = os.path.join(PROBLEMS_DIR, subfolder)
        if os.path.isdir(subfolder_path):
            generate_readme_for_subfolder(subfolder_path)

if __name__ == "__main__":
    generate_readmes()