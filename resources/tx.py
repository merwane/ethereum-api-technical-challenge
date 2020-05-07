from services.ethereum import provider

web3 = provider()

# get details for a specific transaction by txid
def tx_details(txid):
    details = web3.eth.getTransaction(txid)
    details = dict(details)
    data = []
    data.append({
        "blockHash": details["blockHash"].hex(),
        "blockNumber": details["blockNumber"],
        "from": details["from"],
        "gas": details["gas"],
        "gasPrice": details["gasPrice"],
        "hash": details["hash"].hex(),
        "to": details["to"],
        "value": details["value"],
        "url": "https://etherscan.io/tx/"+txid
    })
    return data[0]

# gets transactions between two blocks (range)
# complexity of O(n) // Avoid large ranges
def tx_details_block_range(start_block, end_block):
    transactions = []
    for n in range(start_block, end_block):
        block = web3.eth.getBlock(n)
        details = dict(block)
        for txs in details["transactions"]:
            transactions.append(txs.hex())
    return transactions