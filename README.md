# Ethereum technical challenge
### This is a challenge I had as a part of a recruiting process at a startup building a tokenization solution on top of the Ethereum Blockchain.


## Build a service for querying a blockchain dataset.

Please clone the repo and push changes on a branch. When you think it's ready for review, submit a PR. Feel free to ask questions on here or ping us directly via e-mail. For technical discussions, we'd prefer having them on here.

## Datasets

Each CSV file contains a subset of blockchain historical data

* [Transactions](https://storage.googleapis.com/upvest-development-blockchain-dumps/data/eth-ropsten-transactions.csv) - ethereum-ropsten-history-transaction-staging.csv
  * key fields: blockNumber, blockHash, from/addresses, to
* [Blocks](https://storage.googleapis.com/upvest-development-blockchain-dumps/data/eth-ropsten-blocks.csv) - ethereum-ropsten-history-block-staging.csv
  * key fields: number, hash
* [ERC20 Smart contract balances](https://storage.googleapis.com/upvest-development-blockchain-dumps/data/eth-ropsten-erc20-balance.csv) - ethereum-ropsten-history-erc20-balance-staging.csv
  * key fields: transactionHash, transactionIndex, blockhash, blockNumber, address, contract  
* [Regular Ethereum balances](https://storage.googleapis.com/upvest-development-blockchain-dumps/data/eth-ropsten-eth-balance.csv) - ethereum-ropsten-history-eth-balance-staging.csv -
  * key fields: transactionHash, transactionIndex, blockhash, blockNumber, address


## Public API

* list all transactions with pagination (30 results per page)
* fetch a single transaction
* get the balance of a contract address, including ERC20 Smart contract balances
* list transactions occurring between x & Y dates
* fetch details for a single block 
* get the balance of an address
* fetch details of an address

API supports filtering and sorting results

## Bonus points

* Wrap the resulting code in a ready-to-deploy docker container which runs with docker-compose up
* Use a live Ethereum endpoint instead of the provided CSV files to fetch recent data. 

### Review

We will review your implementation considering the following criteria:

* Resilience (e.g. what happens if an error occurs?)
* Performance (e.g. are there bottlenecks that can be identified without even load testing the application?)
* Clarity (e.g. can I just open the project and get a good insight on the application structure? Is there clear intent in function names?)
* Security (e.g. are there ways that the public API could be abused?)
* Knowledge of the chosen language (e.g. do you demonstrate knowledge of core libraries, and idiomatic coding constructs?)
* Usage of dependencies (e.g. is it worth pulling in an entire package just for a single function?)
* Commit history (e.g. are commit messages clear? does each commit represent a unique and individual change?)

We expect the test task solution to be submitted in either Python, NodeJS/JavaScript, or Go. Tests and deployment strategy are much appreciated. Otherwise we have no other specific requirements and you are free in your design and implementation decisions. 

Comments which can help us understand your rationale are appreciated but not strictly necessary.

Any questions, feel free to ping us.

# My solution

# Notes and instructions for usage:

The API queries both the attached CSV files and the Ethereum mainnet depending on the methods. Querying the CSV file is more optimized when getting all the transactions since we don't have a local copy of the blockchain. All the other methods are using mainnet Ethereum.

## Guide:

After installing the dependencies using Pipfile or pip, launch the developement server by typing `python main.py`

You can also use Docker to build and run an image of the API server.

The used dependencies are `Flask-restful`, `flask-cors` and `web3`.

The local endpoint is the following:
```
http://localhost:5000/api
```

### Get all transactions:
- The transactions are by default paginated and limited to 30 tx details per page.
- You can get all the transactions from the CSV file by doing the following request.
```
/tx/all
```

### Get transaction details by txid:
- You can query the transactions from mainnet by specifying a `txid` as a parameter for the request.
```
/tx/:txid
```

### Get transactions by block range:
- Getting transaction occurring between X & Y dates is not possible without a local node since you cannot query the blocks by timestamp. Also, adding the average mining time to each timestamp to calculate it would be too approximate. This is why I decided to create a block range query method instead.

- You can query the transactions from mainnet by specifying a `start` and `end` block as arguments to the request.

- Be careful, the method is limited to a range of 100 blocks as the complexity of finding each range of transactions for each block and returning them is `O(n)`. This can probably be optimized to `O(log n)` if we had a local node running and a binary seach implemented with it.

```
/api/tx?start=n&end=n
```
- Example usage:
```
/api/tx?start=300000&end=300010
```

### Get balance of specific address:
- You can query an address from mainnet to see its balance by specifying an `address` as a parameter for the request. The default unit is `ether`.

```
/api/address/:address
```

### Get details for a specific block:
- You can get details for a specific block such as the hash or the difficulty by specifying an `number` as a parameter for the request.

```
/api/block/:number
```