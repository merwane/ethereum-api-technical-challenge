from flask_restful import Resource, abort
from flask import request, jsonify
from services.ethereum import transactions
from services.utils import get_paginated_list, block_to_time
from resources.tx import tx_details, tx_details_block_range
from web3.exceptions import TransactionNotFound
from config import BASE_URL

# get all transactions 
# queries from the CSV file as querying mainnet for all txs would take ages without a local ledger ( O(log n) )
class getAllTransactions(Resource):
    def get(self):
        txs = transactions()
        res = get_paginated_list(txs, BASE_URL+"/tx/all", start=request.args.get('start', 1), limit=request.args.get('limit', 30))
        return jsonify(res)

# get a specific tx by txid
# queries from ethereum mainnet
class getTransaction(Resource):
    def get(self, txid):
        try:
            tx = tx_details(txid)
        except TransactionNotFound:
            abort(404, error="TXID not found")
        return jsonify(tx)

# get all transactions between two blocks (range)
# queries from eth mainnet
class getTxByBlockRange(Resource):
    def get(self):
        start_block = request.args.get('start')
        end_block = request.args.get('end')
        # range limited to 100 blocks for performance issues
        if int(end_block) - int(start_block) > 100:
            abort(403, error="Range too large. Please specify a range smaller or equal to 100 blocks.")
        try:  
            details = tx_details_block_range(int(start_block), int(end_block))
        except (ValueError, TypeError):
            abort(401, error="Invalid character or option. Please specify a start block and an end block")
        return jsonify(details)