# ===============================
# S3 ファイルダウンロードスクリプト
# 指定したS3バケットからファイルをダウンロードする
# ===============================

import boto3

def download_file(bucket_name, file_name):
    """
    S3バケットからファイルをダウンロードする関数

    Parameters:
    - bucket_name (str): ダウンロード元のバケット名
    - file_name (str): ダウンロードするファイル名
    """
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, file_name, file_name)
        print(f"File {file_name} downloaded from {bucket_name}.")
    except Exception as e:
        print(f"Error downloading file: {e}")

if __name__ == "__main__":
    bucket_name = input("Enter bucket name: ")
    file_name = input("Enter file name to download: ")
    download_file(bucket_name, file_name)