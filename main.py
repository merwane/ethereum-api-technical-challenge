from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# methods
from controllers.tx import getAllTransactions, getTransaction, getTxByBlockRange
from controllers.address import getBalance
from controllers.block import getBlock

app = Flask(__name__)

# Limit the API to one query endpoint if necessary to avoid spam
CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app)

# routes

# get all transactions (csv)
api.add_resource(getAllTransactions, "/api/tx/all")

# get transaction details by txid (mainnet)
api.add_resource(getTransaction, "/api/tx/<string:txid>")

# get transactions by block range (mainnet)
api.add_resource(getTxByBlockRange, "/api/tx")

# get balance of specific address (mainnet)
api.add_resource(getBalance, "/api/address/<string:address>")

# get details for a specific block (mainnet)
api.add_resource(getBlock, "/api/block/<string:number>")

if __name__ == '__main__':
    app.run(port=5000)
