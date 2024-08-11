"""
CP1404/CP5632 Practical
Project Management Program
Estimate: 90 minutes
Actual:   120 minutes
"""
from datetime import datetime
from project import Project


def main():
    projects = load_projects()
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt")

    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Filename to load: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == 'a':
            project = add_new_project()
            projects.append(project)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? (y/n) ")
            if save_choice.lower() == 'y':
                save_projects("projects.txt", projects)
            else:
                print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice, please try again.")


def load_projects(filename="projects.txt"):
    projects = []
    try:
        with open(filename, 'r') as file:
            file.readline()  # skip header
            for line in file:
                parts = line.strip().split('\t')
                projects.append(Project(*parts))
    except FileNotFoundError:
        print(f"File {filename} does not exist.")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(project)

    print("Completed projects:")
    for project in sorted(complete_projects):
        print(project)


def filter_projects_by_date(projects, date_str):
    date = datetime.strptime(date_str, "%d/%m/%Y")
    filtered_projects = [project for project in projects if project.start_date > date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)


def add_new_project():
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")
    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(project)
    new_completion = input("New Percentage: ")
    if new_completion:
        project.completion_percentage = int(new_completion)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)


main()
