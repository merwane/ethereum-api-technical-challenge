from flask_restful import Resource, abort
from flask import request, jsonify
from resources.balance import address_balance
from web3.exceptions import NameNotFound
from config import BASE_URL


# get balance for a specific address
# queries from eth mainnet; uses ether as unit
class getBalance(Resource):
    def get(self, address):
        try:
            balance = address_balance(address)
        except NameNotFound:
            abort(404, error="Address format is incorrect. Please enter a correct address.")
        return jsonify(balance=balance, unit="ether")