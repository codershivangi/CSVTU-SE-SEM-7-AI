# Agile Sprint Planning

tasks = [
    {"name": "Login Page", "points": 3},
    {"name": "Registration Page", "points": 2},
    {"name": "Database Connection", "points": 5},
    {"name": "Testing", "points": 3},
    {"name": "Documentation", "points": 2}
]

sprint_capacity = 10

selected_tasks = []
total_points = 0

for task in tasks:

    if total_points + task["points"] <= sprint_capacity:

        selected_tasks.append(task)

        total_points += task["points"]


print("AGILE SPRINT PLAN")

print("--------------------")

for task in selected_tasks:

    print(task["name"], "-", task["points"], "Points")


print("--------------------")

print("Total Story Points:", total_points)

print("Remaining Capacity:",
      sprint_capacity - total_points)
