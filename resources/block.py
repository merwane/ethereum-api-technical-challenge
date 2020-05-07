from services.ethereum import provider
import json

web3 = provider()

# get details for a specific block
# latest block by default
def block_details(block_number='latest'):
    block = web3.eth.getBlock(block_number)
    data = []
    transactions = []
    details = dict(block)
    for txs in details["transactions"]:
        transactions.append(txs.hex())
    data.append({
        "difficulty": details["difficulty"],
        "extraData": details["extraData"].hex(),
        "gasLimit": details["gasLimit"],
        "gasUsed": details["gasUsed"],
        "hash": details["hash"].hex(),
        "miner": details["miner"],
        "size": details["size"],
        "timestamp": details["timestamp"],
        "transactions": transactions,

    })
    return data[0]

