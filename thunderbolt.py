# GET http://api_host:port/api/v1/status
# from typing import List
# print(List)
# {
#     "miner": {
#         "devices": [
#             {
#                 "accepted_shares": 2,
#                 "accepted_shares2": 0,
#                 "core_clock": 1620,
#                 "core_utilization": 100,
#                 "fan": 47,
#                 "fidelity1": 5.859799716605649,
#                 "fidelity2": 0,
#                 "hashrate": "217.1 M",
#                 "hashrate2": "36.19 M",
#                 "hashrate2_raw": 36190716.266428046,
#                 "hashrate_raw": 217144297.59856823,
#                 "id": 0,
#                 "info": "GeForce RTX 2070",
#                 "mem_clock": 6801,
#                 "mem_utilization": 86,
#                 "pci_bus_id": 1,
#                 "power": 188,
#                 "rejected_shares": 0,
#                 "rejected_shares2": 0,
#                 "temperature": 72
#             }
# {'algorithm': 'ethash', 'stratum': {'accepted_shares': 0, 'rejected_shares': 0, 'accepted_share_rate': 0,
#  'rejected_share_rate': 0}, 'miners': {'0': {'solver': {'solution_rate': 0}, 'device': {'temperature': 56,
#  'power': 40, 'fan_speed': 38, 'global_memory_used': 478, 'utilization': {'gpu': 2, 'memory': 0}, 'clocks':
# {'core': 1535, 'memory': 6292}, 'pci_bus_id': '0000:10:00.0'}}},
import time
import requests
# import json


import os

phone= 7018411941

def reboot():
    print("REBOOTING")
    os.system("shutdown -t 0 -r -f")

# coin = "ethereum"

def main():
    r= requests.get('http://127.0.0.1:1880/api/status')
    data= r.json()
    start_time = data["start_time"]
    algorithm = data['algorithm']
    accepted_shares = data['stratum']['accepted_shares']
    rejected_shares = data['stratum']['rejected_shares']
    total_hashrate = 0
    for k,v in data['miners'].items():
        total_hashrate += v['solver']['solution_rate']
    
    print(total_hashrate/1000000)
    if total_hashrate<45.00:
        reboot()
    payload= {
    "phone": phone,
    "currentcoin": algorithm,
    "miners" : data['miners'],
        "minerconnected": 1,
    "total_hashrate":total_hashrate,
    
    "start_time":start_time,
    "accepted_shares":accepted_shares,
    "rejected_shares":rejected_shares
    }
    
    requests.post(
        "https://monstermine.herokuapp.com/regulator/call-to-mom/", data=payload)


if __name__ == "__main__":
    while True:
        time.sleep(500)
        main()
        # time.sleep(120)
