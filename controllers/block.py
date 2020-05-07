from flask_restful import Resource, abort
from flask import request, jsonify
from resources.block import block_details
from config import BASE_URL
from web3.exceptions import BlockNotFound


# get details for a specific block
# queries from eth mainnet
class getBlock(Resource):
    def get(self, number):
        try:
            details = block_details(int(number))
        except (ValueError, BlockNotFound):
            abort(400, error="The block doesn't exist yet or the query is incorrect.")
        return jsonify(details)