# ===============================
# S3 ファイルアップロードスクリプト
# AWSのS3バケットに指定したファイルをアップロードする
# ===============================

import boto3

def upload_file(bucket_name, file_name):
    """
    S3バケットにファイルをアップロードする関数

    Parameters:
    - bucket_name (str): アップロード先のバケット名
    - file_name (str): アップロードするファイル名
    """
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        print(f"File {file_name} uploaded to {bucket_name}.")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    # ユーザー入力を受け取る
    bucket_name = input("Enter bucket name: ")
    file_name = input("Enter file name to upload: ")
    upload_file(bucket_name, file_name)