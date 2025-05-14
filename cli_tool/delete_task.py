import json
import os

TASK_FILE = "tasks.json"

def delete_task():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)

        if not tasks:
            print("削除できるタスクがありません。")
            return

        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

        index = int(input("削除したいタスクの番号を入力してください: ")) - 1

        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            with open(TASK_FILE, "w") as file:
                json.dump(tasks, file)

            print(f"タスク '{deleted_task}' を削除しました！")
        else:
            print("無効な番号です。")

    except FileNotFoundError:
        print("タスクファイルが存在しません。")

if __name__ == "__main__":
    delete_task()