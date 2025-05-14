# ===============================
# EC2 起動・停止スクリプト
# 指定したEC2インスタンスを起動または停止する
# ===============================

import boto3

def control_ec2(instance_id, action):
    """
    EC2インスタンスを起動または停止する関数

    Parameters:
    - instance_id (str): インスタンスID
    - action (str): "start" または "stop"
    """
    ec2 = boto3.client('ec2')
    try:
        if action == "start":
            ec2.start_instances(InstanceIds=[instance_id])
            print(f"Instance {instance_id} started.")
        elif action == "stop":
            ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Instance {instance_id} stopped.")
        else:
            print("Invalid action. Use 'start' or 'stop'.")
    except Exception as e:
        print(f"Error in EC2 control: {e}")

if __name__ == "__main__":
    instance_id = input("Enter EC2 instance ID: ")
    action = input("Enter action (start/stop): ")
    control_ec2(instance_id, action)