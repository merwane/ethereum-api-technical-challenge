from services.ethereum import provider

web3 = provider()

# balance for a specific address
# by default in ether
def address_balance(address, currency="ether"):
    query = web3.eth.getBalance(address)
    balance = web3.fromWei(query, currency)
    return float(balance)

