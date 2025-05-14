# ===============================
# S3 ファイル一覧取得スクリプト
# 指定したS3バケット内のファイルをリスト表示する
# ===============================

import boto3

def list_files(bucket_name):
    """
    S3バケット内のファイル一覧を取得する関数

    Parameters:
    - bucket_name (str): バケット名
    """
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        # ファイル一覧を表示
        for obj in response.get('Contents', []):
            print(obj['Key'])
    except Exception as e:
        print(f"Error listing files: {e}")

if __name__ == "__main__":
    bucket_name = input("Enter bucket name: ")
    list_files(bucket_name)