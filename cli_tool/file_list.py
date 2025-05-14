# ===============================
# ファイル一覧取得ツール
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
        if not os.path.exists(directory):
            print(f"ディレクトリ '{directory}' が見つかりません。")
            return

        files = os.listdir(directory)
        if files:
            for file in files:
                print(file)
        else:
            print(f"'{directory}' 内にはファイルがありません。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    directory = input("Enter directory path: ")
    list_files(directory)