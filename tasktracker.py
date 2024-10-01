import json
import os
import sys

TASK = 'task.json'

def load_task():
    if not os.path.exists(TASK):
        return []
    with open(TASK, 'r') as file:
        return json.load(file)
    
def save_task(task):
    with open(TASK, 'w') as file:
        json.dump(task, file, indent = 4)

def add_task(description):
    tasks = load_task()
    task = {
        'id' : len(tasks) + 1,
        'description': description,
        'status' : 'todo'
    }
    tasks.append(task)
    save_task(tasks)
    print(f"Task added successfully (ID:{task['id']})")

def uptade_task(task_id, description):
    tasks = load_task()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            save_task(tasks)
            print(f"Task updated successfully(ID:{task_id})")
            return 
    print("Task not found.")

def delete_task(task_id):
    tasks = load_task()
    uptade_tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) == len(uptade_tasks):
        print("Task not found.")
    else:
        save_task(uptade_tasks)
        print(f"Task deleted successfully (ID:{task_id})")

def mark_task(task_id, status):
    tasks = load_task()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            save_task(tasks)
            print(f"Task marked as {status} (ID: {task_id})")
            return
    print("Task not found.")

def list_tasks(status = None):
    tasks = load_task()
    if status:
        filtered_tasks = [task for task in tasks if task['status'] == status]
        if filtered_tasks:
            for task in filtered_tasks:
                print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")
        else:
            print(f"No tasks with status '{status}'.")
    else:
        if tasks:
            for task in tasks:
                print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")
        else:
            print(f"No tasks with status '{status}'.")

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli [command][arguments]")
        return
    command = sys.argv[1].lower()
    if command == 'add':
        if len(sys.argv) < 3:
            print("Usage: task-cli add [description]")
            return
        add_task(sys.argv[2])
    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: task-cli update [id] [description]")
            return
        uptade_task(int(sys.argv[2]), sys.argv[3])
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: task-cli delete [id]")
            return
        delete_task(int(sys.argv[2]))
    elif command == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-in-progress [id]")
            return 
        mark_task(int(sys.argv[2]), 'in-progress')
    elif command == 'mark-done':
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-done [id]")
            return
        mark_task(int(sys.argv[2], 'done'))
    elif command == 'list':
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print("Unknown command.")
if __name__ == "__main__":
    main()