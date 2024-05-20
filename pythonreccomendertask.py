# Define a task class
class Task:
  def __init__(self, name, description, priority=0):
    self.name = name
    self.description = description
    self.priority = priority  # Higher number means higher priority

  def __str__(self):
    return f"{self.priority} - {self.name} - {self.description}"

# Global task list
tasks = []

def add_task():
  """Prompts user for task details and adds it to the list"""
  name = input("Enter task name: ")
  description = input("Enter task description: ")
  priority = int(input("Enter priority (higher number = higher priority): "))
  tasks.append(Task(name, description, priority))
  print("Task added successfully!")

def remove_task():
  """Removes a task by index"""
  if not tasks:
    print("No tasks to remove!")
    return
  list_tasks()
  index = int(input("Enter index of the task to remove: "))
  if index < 0 or index >= len(tasks):
    print("Invalid index!")
  else:
    del tasks[index]
    print("Task removed successfully!")

def list_tasks():
  """Prints all tasks in the list"""
  if not tasks:
    print("No tasks found!")
  else:
    print("Your tasks:")
    for i, task in enumerate(tasks):
      print(f"{i}. {task}")

def prioritize_task():
  """Allows changing priority of a task"""
  if not tasks:
    print("No tasks to prioritize!")
    return
  list_tasks()
  index = int(input("Enter index of the task to prioritize: "))
  if index < 0 or index >= len(tasks):
    print("Invalid index!")
  else:
    new_priority = int(input("Enter new priority: "))
    tasks[index].priority = new_priority
    print("Task priority updated!")

def recommend_tasks():
  """Recommends tasks based on keywords in descriptions"""
  keyword = input("Enter a keyword to search for: ")
  recommendations = []
  for task in tasks:
    if keyword.lower() in task.description.lower():
      recommendations.append(task)
  if recommendations:
    print("Recommended tasks:")
    for task in recommendations:
      print(task)
  else:
    print(f"No tasks found containing '{keyword}'.")

def main():
  while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Prioritize Task")
    print("5. Recommend Tasks")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      add_task()
    elif choice == '2':
      remove_task()
    elif choice == '3':
      list_tasks()
    elif choice == '4':
      prioritize_task()
    elif choice == '5':
      recommend_tasks()
    elif choice == '6':
      print("Exiting...")
      break
    else:
      print("Invalid choice!")

if __name__ == "__main__":
  main()
