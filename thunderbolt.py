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
import requests
import json

phone = 7018411941
coin = "ethereum"

def main():
    r = requests.get('http://127.0.0.1:1880/api/v1/status')
    data = r.json()
    # if 
    print(data)
    payload = {
    "phone": phone,
    "currentcoin": coin,
    "minespeed" :data["miner"]["devices"][0]["hashrate"],
        "minerconnected" : 1
    }

    requests.post("https://monstermine.herokuapp.com/regulator/call-to-mom/", data=payload)


if __name__ == "__main__":
    main()