from web3 import Web3
import csv
import json
from config import ETH_ENDPOINT

# eth mainnet provider
def provider():
    web3 = Web3(Web3.HTTPProvider(ETH_ENDPOINT))
    return web3

# fetches transactions from the CSV file
def transactions():
    tx_csv = open("data/transactions.csv", "r")
    fieldnames = ("index", "addresses", "blockHash", "blockNumber", "from", "hash", "input")
    reader = csv.DictReader(tx_csv, fieldnames)
    data = []
    for row in reader:
        data.append({
            "addresses": row["addresses"],
            "blockHash": row["blockHash"],
            "blockNumber": row["blockNumber"],
            "from": row["from"],
            "hash": row["hash"],
            "input": row["input"]
        })
    del data[0]
    return data

# fetches contracts from the CSV file
def contracts():
    contract_csv = open("data/contracts.csv", "r")
    fieldnames = ("index", "address", "blockHash", "blockNumber", "contract", "isMainChain", "payload", "transactionHash", "transactionIndex", "uuid")
    reader = csv.DictReader(contract_csv, fieldnames)
    data = []
    for row in reader:
        data.append({
            "address": row["address"],
            "blockHash": row["blockHash"],
            "blockNumber": row["blockNumber"],
            "contract": row["contract"],
            "isMainChain": row["isMainChain"],
            "payload": row["payload"],
            "transactionHash": row["transactionHash"],
            "transactionIndex": row["transactionIndex"],
            "uuid": row["uuid"]
        })
    del data[0]
    return data
