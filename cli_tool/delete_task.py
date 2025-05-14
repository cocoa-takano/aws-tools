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

        for task in tasks:
            print(f"ID: {task['id']} - {task['task']}")

        try:
            task_id = int(input("削除したいタスクのIDを入力してください: "))
            task_index = next((i for i, t in enumerate(tasks) if t["id"] == task_id), None)

            if task_index is not None:
                deleted_task = tasks.pop(task_index)
                with open(TASK_FILE, "w") as file:
                    json.dump(tasks, file)
                print(f"タスク '{deleted_task['task']}' を削除しました！")
            else:
                print("無効なIDです。")

        except ValueError:
            print("数字で入力してください。")

    except FileNotFoundError:
        print("タスクファイルが存在しません。")

if __name__ == "__main__":
    delete_task()