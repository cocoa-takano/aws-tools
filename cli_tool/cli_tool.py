# ===============================
# CLI ツール
# 指定したディレクトリ内のファイル一覧を表示する
# ===============================

import os

def list_files(directory):
    """
    指定したディレクトリ内のファイル一覧を表示する関数

    Parameters:
    - directory (str): ディレクトリパス
    """
    try:
        files = os.listdir(directory)
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error listing files: {e}")

if __name__ == "__main__":
    directory = input("Enter directory path: ")
    list_files(directory)