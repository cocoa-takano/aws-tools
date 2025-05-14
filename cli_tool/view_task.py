import json

TASK_FILE = "tasks.json"

def view_task():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)

        if not tasks:
            print("タスクはありません。")
        else:
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")

    except FileNotFoundError:
        print("タスクファイルが存在しません。")

if __name__ == "__main__":
    view_task()