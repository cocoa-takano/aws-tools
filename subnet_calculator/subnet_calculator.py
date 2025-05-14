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
        # '/' が含まれない場合は '/32' を追加
        if '/' not in cidr:
            cidr += '/32'
        
        network = ipaddress.ip_network(cidr, strict=False)
        print(f"Network:      {network.network_address}")
        print(f"Broadcast:    {network.broadcast_address}")
        print(f"Total Hosts:  {network.num_addresses}")
        
        # 有効ホスト数の計算
        if network.num_addresses > 2:
            usable_hosts = network.num_addresses - 2
        else:
            usable_hosts = network.num_addresses  # /31, /32 の場合はそのまま
        
        print(f"Usable Hosts: {usable_hosts}")

    except ValueError as e:
        print(f"Invalid CIDR: {e}")

if __name__ == "__main__":
    cidr = input("Enter CIDR (e.g., 192.168.1.0/24): ").strip()
    calculate_subnet(cidr)