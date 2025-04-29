from dotenv import load_dotenv

from eth_account import Account
from web3.utils.coti import CotiNetwork, generate_or_recover_aes, init_web3

from utils import (
    get_account_private_key,
    set_account_encryption_key
)


# Script onboards a EOA -  Externally Owned Account (EOA)
# into the network, meaning, creates a AES key unique to that user,
# and that key will be used to encrypt all data sent back to the wallet
# mandatory script for any operation done in a contract that requires
# encrypt/decrypt (which is basically all new precompiles operations introduced)
def main():
    eoa, web3 = init()

    generate_or_recover_aes(web3, eoa)
    env_value = set_account_encryption_key(eoa.aes_key)

    if env_value[0] is not True:
        raise Exception('encryption key not saved in .env!')
    


def init():
    load_dotenv()  # loading .env
    eoa_private_key = get_account_private_key()  # Get EOA Private key for execution
    eoa = Account.from_key(eoa_private_key)  # Get EOA

    # Define methods expected by coti utils
    def set_user_onboard_info(self, info):
        self.user_onboard_info = info
        self.rsa_key_pair = info.get("rsa_key_pair")
        self.onboard_tx_hash = info.get("tx_hash")
        self.aes_key = info.get("aes_key")

    def set_aes_key(self, key):
        self.aes_key = key

    # Dynamically attach methods and attributes to the LocalAccount instance
    eoa.set_user_onboard_info = set_user_onboard_info.__get__(eoa, Account)
    eoa.set_aes_key = set_aes_key.__get__(eoa, Account)
    eoa.user_onboard_info = None
    eoa.aes_key = None
    eoa.rsa_key_pair = None
    eoa.onboard_tx_hash = None

    web3 = init_web3(CotiNetwork.TESTNET)  # Init connection to node
    return eoa, web3


if __name__ == "__main__":
    main()
