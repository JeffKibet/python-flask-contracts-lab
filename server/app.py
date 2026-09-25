#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"}]  # keep your full list here
customers = ["bob", "bill", "john", "sarah"]
app = Flask(__name__)


@app.route('/contract/<int:id>')
def get_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return contract["contract_information"], 200
    return make_response("Contract not found", 404)


@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    if customer_name in customers:
        return make_response('', 204)
    return make_response("Customer not found", 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)