#AWS Tools Project

## プロジェクト概要
AWS環境の基本操作およびネットワーク計算を行うPythonスクリプト集です。  
学習の一環として作成し、AWS S3のファイル管理（アップロード、ダウンロード、ファイル一覧取得）、EC2インスタンスの制御、サブネット計算、ローカルファイル管理ツールを実装しました。  

また、タスク管理用の `tasks.json` ファイルは `cli_tool` フォルダ内に格納されています。  
初期状態の `tasks.json` は空の配列 (`[]`) ですが、スクリプト実行によりタスクが追加されます。

---

## 動作環境

- Python 3.11  
- `boto3` ライブラリを使用  

---

### ツール一覧

#### 1. S3ファイル管理ツール (`s3_manager/`)  
AWS S3バケット内のファイル管理を行うスクリプト群です。

- **upload_s3.py**：S3バケットにファイルをアップロード  
- **download_s3.py**：S3バケットからファイルをダウンロード  
- **list_s3.py**：S3バケット内のファイル一覧を取得  

---

#### 2. EC2管理ツール (`ec2_manager/`)  
AWS EC2インスタンスの起動および停止を行うスクリプトです。

- **ec2_control.py**：指定したインスタンスIDを起動または停止  

---

#### 3. サブネット計算ツール (`subnet_calculator/`)  
CIDR表記のIPアドレスからネットワーク情報を取得するスクリプトです。

- **subnet_calculator.py**：CIDRからネットワークアドレス、ブロードキャストアドレス、ホスト数を取得  

---

#### 4. CLIツール (`cli_tool/`)  
ローカルディレクトリ内のファイル一覧を取得するスクリプトと、タスク管理ツールを含みます。

- **file_list.py**：指定したフォルダ内のファイル一覧を表示  
- **add_task.py**：タスクを追加  
- **view_task.py**：タスクの一覧を表示  
- **delete_task.py**：タスクを削除   

---

### 使い方

---

#### **S3関連の操作**

- S3にファイルをアップロード

```bash
python s3_manager/upload_s3.py
```

- S3からファイルをダウンロード  

```bash
python s3_manager/download_s3.py
```

- S3のファイル一覧を取得    

```bash
python s3_manager/list_s3.py
```  

---

####  **EC2関連の操作**

- EC2インスタンスの起動/停止  

```bash
python ec2_manager/ec2_control.py
```

---

####  **サブネット情報の取得**

- サブネットのCIDR情報を取得  

```bash
python subnet_calculator/subnet_calculator.py
```

---

####  **ローカルファイル一覧の取得**

- ローカルディレクトリ内のファイル一覧を取得  

```bash
python cli_tool/file_list.py
```  

---

#### **タスク管理ツール**

- タスクを追加

```bash
python cli_tool/add_task.py
```

- タスクの一覧を表示

```bash
python cli_tool/view_task.py
```

- タスクを消去

```bash
python cli_tool/delete_task.py
```
