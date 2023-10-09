#import the Web3 module from Web3 library
from web3 import Web3
url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3=Web3(Web3.HTTPProvider(url))
lb=web3.eth.get_block("latest")
print("latest block is :",lb)
btc=web3.eth.get_block_transaction_count(18312808)
print("number of transaction happened:",btc)
tf=web3.eth.fee_history(4,"latest",None)
print("transaction fee :",tf)