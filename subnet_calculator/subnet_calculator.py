# ===============================
# サブネット計算ツール
# CIDR表記のIPアドレスからネットワーク情報を取得する
# ===============================

import ipaddress

def calculate_subnet(cidr):
    """
    サブネット情報を計算して表示する関数

    Parameters:
    - cidr (str): CIDR表記のアドレス（例: "192.168.1.0/24"）
    """
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        print(f"Network: {network.network_address}")
        print(f"Broadcast: {network.broadcast_address}")
        print(f"Total Hosts: {network.num_addresses}")
    except ValueError as e:
        print(f"Invalid CIDR: {e}")

if __name__ == "__main__":
    cidr = input("Enter CIDR (e.g., 192.168.1.0/24): ")
    calculate_subnet(cidr)