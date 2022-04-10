from web3 import Web3
from threading import Timer, Thread, Event
import warnings
warnings.filterwarnings("ignore")


class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(0.1):
            # bsc = https://bsc-dataseed.binance.org/
            # eth = https://mainnet.infura.io/v3/

            bsc = 'https://bsc-dataseed.binance.org/'
            web3 = Web3(Web3.HTTPProvider(bsc, request_kwargs={'verify': False}))
            # print(web3.isConnected())
           
            account_1 = '.........'
            private_key1 = '..........'
            account_2 = '.........'
            balance = web3.eth.get_balance(account_1)
            human_readable = web3.fromWei(balance, 'ether')
            print("Balance BNB : " + str(human_readable))
            if human_readable > 0.00001:
                nonce = web3.eth.getTransactionCount(account_1)
                tx = {
                    'nonce': nonce,
                    'to': account_2,
                    'value': web3.toWei(balance, 'ether'),
                    'gas': 21000,
                    'gasPrice': web3.toWei(5, 'gwei'),

                }
                signed_tx = web3.eth.account.sign_transaction(tx, private_key1)
                tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                print(web3.toHex(tx_hash))


stopFlag = Event()
thread = MyThread(stopFlag)
thread.start()
