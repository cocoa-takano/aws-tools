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

    tasks.append(task)

    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)

    print("タスクが追加されました！")

if __name__ == "__main__":
    add_task()