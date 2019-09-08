import pywaves as pw


NODE = "https://testnode1.wavesnodes.com"
CHAIN = 'testnet'
pw.setNode(node=NODE, chain=CHAIN)
DAPPADDRESS = "3N18S8xfWJYHVuGfJcpcPVh7LsnqR9hKTcc"

MAX2_PRIVATEKEY = "CtsaSnAPoVMupqGyk4b4qpgXKH2nSs4rG7GujdPeXvco"
MAX1_PRIVATEKEY = "4FRCTx52VzFKTk1F38AHfsXKFhwChd9gKf4Ef3LzzpY4"


args = [
    {"type": "integer", "value": 1, },
    {"type": "integer", "value": 2, },
    {"type": "integer", "value": 3, },
    {"type": "integer", "value": 4, },
    {"type": "integer", "value": 5, },
    {"type": "integer", "value": 6, },
    {"type": "integer", "value": 17, },
    {"type": "integer", "value": 18, },
    {"type": "integer", "value": 19, },
    {"type": "integer", "value": 20, },
    {"type": "integer", "value": 39, },
    {"type": "integer", "value": 100, }
]


def invoke_remote_script(funcName, args, price, privateKey):
    address = pw.Address(privateKey=privateKey)

    tx = address.invokeScript(DAPPADDRESS, funcName,
                              args,
                              [{"amount": price, "assetId": None}])
    return tx




def create_patent(coords, privateKey):
    PRICE = 100000000
    FUNC = "patent"
    tx = invoke_remote_script(FUNC, coords, PRICE, privateKey)
    print(tx)

def buy_patent(coords, privateKey):
    FUNC = "buyPatent"
    PATENT_PRICE = 200000000
    tx = invoke_remote_script(FUNC, coords, PATENT_PRICE, privateKey)
    print(tx)

def withdraw(privateKey):
    FUNC = "withdraw"
    tx = invoke_remote_script(FUNC, [], [], privateKey)
    print(tx)



import time
create_patent(args,MAX1_PRIVATEKEY)
time.sleep(5)
buy_patent(args,MAX2_PRIVATEKEY)
time.sleep(5)
withdraw(MAX1_PRIVATEKEY)