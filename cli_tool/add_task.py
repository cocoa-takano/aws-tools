import json
import os

TASK_FILE = "tasks.json"

def add_task():
    task = input("追加するタスクを入力してください: ")

    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)
    else:
        tasks = []

    new_id = 1 if not tasks else tasks[-1]["id"] + 1
    tasks.append({"id": new_id, "task": task})

    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)

    print(f"タスク '{task}' が追加されました！（ID: {new_id}）")

if __name__ == "__main__":
    add_task()